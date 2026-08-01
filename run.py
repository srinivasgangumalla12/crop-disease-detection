"""
Main Application Launcher for KrishiRakshak AI - Crop Disease & Weather Advisory System.
"""

import sys
import os
import uvicorn

# Force UTF-8 output encoding for Windows terminal compatibility
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("\n" + "="*70)
    print("Starting KrishiRakshak AI - Crop Disease Detection & Advisory Server")
    print("Local Web Dashboard: http://localhost:8000")
    print("OpenAPI Documentation: http://localhost:8000/docs")
    print("="*70 + "\n")
    
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=False)
