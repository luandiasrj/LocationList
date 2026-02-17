
import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# Add project root to sys.path - Fix relative import issues
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.services.ai_service import verificar_cidade_com_ia

def test_ai_single():
    print("--- AI Test Script ---")
    
    # Load .env
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
    load_dotenv(env_path)
    
    api_key = os.getenv("AI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: AI_API_KEY not found in .env")
        return

    # Configure GenAI
    genai.configure(api_key=api_key)
    
    print("\n1. Listing Available Models (Managed internally by Service)")

    print("\n2. Testing City Verification (São Paulo):")
    cidade = "São Paulo"
    estado = "SP"
    # Simulated API response for São Paulo
    locations = [
        {"name": "São Paulo", "adm1": "São Paulo", "adm2": "São Paulo", "id": "1012345", "lat": "-23.55", "lon": "-46.63", "fxLink": "http://example.com/sp"},
        {"name": "São Pedro", "adm1": "São Paulo", "adm2": "São Pedro", "id": "1012346", "lat": "-22.55", "lon": "-47.63", "fxLink": "http://example.com/spedro"}
    ]
    
    try:
        import asyncio
        if sys.platform == 'win32':
             asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
             
        result = asyncio.run(verificar_cidade_com_ia(cidade, estado, locations, manual_mode=False))
        print(f" Result: {result}")
    except Exception as e:
        print(f" Error during test: {e}")

if __name__ == "__main__":
    test_ai_single()
