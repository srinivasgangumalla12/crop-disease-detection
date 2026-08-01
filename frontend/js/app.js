// Frontend Interactive Application Logic for FARMERS SOLUTION

document.addEventListener("DOMContentLoaded", () => {

  // State
  let currentFile = null;
  let lastDiagnosticReport = null;
  let speechSynth = window.speechSynthesis;

  // DOM Elements
  const tabButtons = document.querySelectorAll(".nav-tab");
  const tabPanes = document.querySelectorAll(".tab-pane");

  const dropZone = document.getElementById("drop-zone");
  const fileInput = document.getElementById("file-input");
  const previewWrapper = document.getElementById("preview-wrapper");
  const imagePreview = document.getElementById("image-preview");
  const btnRemoveImage = document.getElementById("btn-remove-image");
  const btnAnalyze = document.getElementById("btn-analyze");

  const selectRegion = document.getElementById("select-region");
  const selectLang = document.getElementById("select-lang");
  const btnThemeToggle = document.getElementById("btn-theme-toggle");

  const diagnosisLoading = document.getElementById("diagnosis-loading");
  const diagnosisEmpty = document.getElementById("diagnosis-empty");
  const diagnosisResult = document.getElementById("diagnosis-result");
  const btnSpeakVoice = document.getElementById("btn-speak-voice");

  // Tab Navigation
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetTab = btn.getAttribute("data-tab");
      tabButtons.forEach(b => b.classList.remove("active"));
      tabPanes.forEach(p => p.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById(targetTab).classList.add("active");
    });
  });

  // Theme Toggle
  btnThemeToggle.addEventListener("click", () => {
    document.body.classList.toggle("theme-light");
    document.body.classList.toggle("theme-dark");
  });

  // File Input & Drag and Drop Handling
  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) {
      setFileForAnalysis(e.target.files[0]);
    }
  });

  dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragover");
  });

  dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragover");
  });

  dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragover");
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      setFileForAnalysis(e.dataTransfer.files[0]);
    }
  });

  btnRemoveImage.addEventListener("click", (e) => {
    e.stopPropagation();
    resetImageSelection();
  });

  function resetImageSelection() {
    currentFile = null;
    fileInput.value = "";
    imagePreview.src = "";
    previewWrapper.classList.add("hidden");
    dropZone.querySelector(".drop-zone-content").classList.remove("hidden");
    btnAnalyze.disabled = true;
  }

  function setFileForAnalysis(file) {
    currentFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.src = e.target.result;
      dropZone.querySelector(".drop-zone-content").classList.add("hidden");
      previewWrapper.classList.remove("hidden");
      btnAnalyze.disabled = false;
    };
    reader.readAsDataURL(file);
  }

  // Quick Sample Buttons (1-Click Test)
  const sampleBtns = document.querySelectorAll(".sample-btn");
  sampleBtns.forEach(btn => {
    btn.addEventListener("click", async () => {
      const sampleFileName = btn.getAttribute("data-sample");
      try {
        // Fetch sample file from backend static create_samples folder
        const res = await fetch(`/api/sample_image?name=${sampleFileName}`);
        if (!res.ok) {
          // Fallback fetch from static
          const imageRes = await fetch(`/static/sample_leaf.jpg`);
        }
        // Convert to blob file
        const imageBlob = await fetch(`/api/sample_image?name=${sampleFileName}`).then(r => r.blob());
        const file = new File([imageBlob], sampleFileName, { type: "image/jpeg" });
        setFileForAnalysis(file);
        // Trigger auto analyze
        analyzeCropLeaf();
      } catch (err) {
        console.log("Loading sample...", sampleFileName);
        // Fetch direct endpoint
        const blob = await fetch(`/api/sample_image?name=${sampleFileName}`).then(r => r.blob());
        const file = new File([blob], sampleFileName, { type: "image/jpeg" });
        setFileForAnalysis(file);
        analyzeCropLeaf();
      }
    });
  });

  // Analyze Button Event
  btnAnalyze.addEventListener("click", () => {
    if (currentFile) {
      analyzeCropLeaf();
    }
  });

  // Main Diagnosis Function
  async function analyzeCropLeaf() {
    if (!currentFile) return;

    // Show Loading
    diagnosisEmpty.classList.add("hidden");
    diagnosisResult.classList.add("hidden");
    diagnosisLoading.classList.remove("hidden");
    btnSpeakVoice.classList.add("hidden");

    const formData = new FormData();
    formData.append("file", currentFile);
    formData.append("region", selectRegion.value);
    formData.append("lang", selectLang.value);

    try {
      const response = await fetch("/api/detect", {
        method: "POST",
        body: formData
      });

      if (!response.ok) {
        throw new Error("Diagnostic API error");
      }

      const report = await response.json();
      lastDiagnosticReport = report;

      // Render Diagnostic Report
      renderDiagnosisReport(report);

      // Auto Voice Speak Aloud ("Farmer keeps photo then it has to tell")
      speakDiagnosticAudio(report);

    } catch (err) {
      alert("Error processing crop leaf analysis. Please try again.");
    } finally {
      diagnosisLoading.classList.add("hidden");
      diagnosisResult.classList.remove("hidden");
    }
  }

  // Render Diagnostic Results
  function renderDiagnosisReport(report) {
    document.getElementById("res-crop-badge").textContent = report.crop || "Crop";
    document.getElementById("res-disease-name").textContent = report.disease_name || "Leaf Disease";
    document.getElementById("res-category").textContent = report.category || "Fungal";
    document.getElementById("res-confidence").textContent = `${report.confidence_score}%`;
    document.getElementById("res-severity").textContent = report.severity_level || "Moderate";
    document.getElementById("res-affected-area").textContent = `${report.affected_area_percentage}%`;

    const weatherRiskScore = report.weather_advisory?.disease_spreading_risk_score || 75;
    document.getElementById("res-weather-risk").textContent = `${weatherRiskScore}% Risk`;

    // Organic Remedies List
    const orgList = document.getElementById("res-organic-list");
    orgList.innerHTML = "";
    (report.organic_remedies || []).forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      orgList.appendChild(li);
    });

    // Chemical Remedies List
    const chemList = document.getElementById("res-chemical-list");
    chemList.innerHTML = "";
    (report.chemical_remedies || []).forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      chemList.appendChild(li);
    });

    // Weather Warning & Action Steps
    const wWarning = document.getElementById("res-weather-warning");
    wWarning.textContent = report.weather_advisory?.specific_warning || "Monitor micro-climate conditions.";

    const actionList = document.getElementById("res-action-list");
    actionList.innerHTML = "";
    (report.weather_advisory?.action_steps || []).forEach(step => {
      const li = document.createElement("li");
      li.textContent = step;
      actionList.appendChild(li);
    });

    // Show Voice Button
    btnSpeakVoice.classList.remove("hidden");
  }

  // Text-To-Speech (TTS) Voice Readout Functionality
  btnSpeakVoice.addEventListener("click", () => {
    if (lastDiagnosticReport) {
      speakDiagnosticAudio(lastDiagnosticReport);
    }
  });

  function speakDiagnosticAudio(report) {
    if (!speechSynth) return;

    // Stop ongoing speech
    speechSynth.cancel();

    const speechText = report.audio_speech_text || `${report.crop} disease identified as ${report.disease_name}.`;
    const utterance = new SpeechSynthesisUtterance(speechText);

    // Map language BCP-47 tags (e.g. te-IN for Telugu, hi-IN for Hindi)
    const langCode = report.selected_lang?.bcp47 || "en-US";
    utterance.lang = langCode;
    utterance.rate = 0.9; // Slightly calm speed for farmers
    utterance.pitch = 1.0;

    speechSynth.speak(utterance);
  }

  // Language Change Event Handler
  selectLang.addEventListener("change", () => {
    if (lastDiagnosticReport && currentFile) {
      // Re-run diagnosis to get translated report & speech text
      analyzeCropLeaf();
    }
  });

  // Region Change Event Handler
  selectRegion.addEventListener("change", () => {
    fetchWeatherForRegion(selectRegion.value);
  });

  // Weather Fetch Function
  async function fetchWeatherForRegion(regionName) {
    try {
      const res = await fetch(`/api/weather?region=${encodeURIComponent(regionName)}`);
      if (res.ok) {
        const data = await res.json();
        const w = data.weather;
        const adv = data.advisory;

        document.getElementById("w-temp").textContent = `${w.current_temperature} °C`;
        document.getElementById("w-humidity").textContent = `${w.relative_humidity} %`;
        document.getElementById("w-rain").textContent = `${w.rain_prob_pct} %`;
        document.getElementById("w-wind").textContent = `${w.wind_speed_kmh} km/h`;

        const riskBadge = document.getElementById("risk-badge");
        const riskFill = document.getElementById("risk-progress-fill");

        riskBadge.textContent = `${adv.risk_category} (${adv.disease_spreading_risk_score}%)`;
        riskFill.style.width = `${adv.disease_spreading_risk_score}%`;
        document.getElementById("risk-description").textContent = adv.action_steps[0] || "Normal agricultural weather.";
      }
    } catch (e) {
      console.log("Weather fetch fallback active.");
    }
  }

  document.getElementById("btn-refresh-weather").addEventListener("click", () => {
    fetchWeatherForRegion(selectRegion.value);
  });

  // WhatsApp Bot Simulator Interaction
  const waBtnSend = document.getElementById("wa-btn-send");
  const waInput = document.getElementById("wa-text-input");
  const waChatBody = document.getElementById("wa-chat-body");

  waBtnSend.addEventListener("click", sendWhatsAppMessage);
  waInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendWhatsAppMessage();
  });

  function sendWhatsAppMessage() {
    const text = waInput.value.trim();
    if (!text) return;

    // Render User Message
    const userMsg = document.createElement("div");
    userMsg.className = "wa-msg wa-sent";
    userMsg.innerHTML = `
      <div class="wa-bubble">${text}</div>
      <span class="wa-time">Now</span>
    `;
    waChatBody.appendChild(userMsg);
    waInput.value = "";
    waChatBody.scrollTop = waChatBody.scrollHeight;

    // Simulate WhatsApp Bot Response
    setTimeout(async () => {
      const botMsg = document.createElement("div");
      botMsg.className = "wa-msg wa-received";

      let botText = "🌾 *FARMERS SOLUTION Bot*: Processing your query...";
      if (text.toLowerCase().includes("weather")) {
        botText = `🌤️ *Live Farm Weather Report for ${selectRegion.value}*\nTemp: ${document.getElementById("w-temp").textContent}\nHumidity: ${document.getElementById("w-humidity").textContent}\nFungal Risk: HIGH (82%). Spray before rains.`;
      } else if (text.toLowerCase().includes("telugu") || text.toLowerCase().includes("తెలుగు")) {
        selectLang.value = "te";
        botText = "✅ భాష తెలుగులోకి మార్చబడింది. మీ పంట ఆకు ఫోటో పంపండి.";
      } else {
        botText = "🌾 Please upload or select a leaf sample image to get full WhatsApp disease diagnosis and remedy card.";
      }

      botMsg.innerHTML = `
        <div class="wa-bubble">${botText}</div>
        <span class="wa-time">Now</span>
      `;
      waChatBody.appendChild(botMsg);
      waChatBody.scrollTop = waChatBody.scrollHeight;
    }, 600);
  }

  // Local Dataset Upload Form
  const dsForm = document.getElementById("form-dataset-upload");
  if (dsForm) {
    dsForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const file = document.getElementById("ds-file").files[0];
      const crop = document.getElementById("ds-crop").value;
      const disease = document.getElementById("ds-disease").value;
      const location = document.getElementById("ds-location").value;

      if (!file) return;

      const fd = new FormData();
      fd.append("file", file);
      fd.append("crop_name", crop);
      fd.append("disease_tag", disease);
      fd.append("location", location);

      try {
        const res = await fetch("/api/dataset/upload", {
          method: "POST",
          body: fd
        });
        const data = await res.json();
        alert(data.message || "Local farm photo uploaded!");
        loadDatasetGallery();
      } catch (err) {
        alert("Upload error.");
      }
    });
  }

  async function loadDatasetGallery() {
    try {
      const res = await fetch("/api/dataset/list");
      if (res.ok) {
        const data = await res.json();
        const gallery = document.getElementById("dataset-gallery");
        if (data.photos && data.photos.length > 0) {
          gallery.innerHTML = "";
          data.photos.forEach(p => {
            const div = document.createElement("div");
            div.className = "gallery-item";
            div.innerHTML = `<img src="${p.url}" alt="${p.filename}"><p>${p.filename}</p>`;
            gallery.appendChild(div);
          });
        }
      }
    } catch (e) {}
  }

  // Initial Weather Load
  fetchWeatherForRegion(selectRegion.value);

});
