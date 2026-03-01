from config import get_gemini_model
from storage import save_history, load_history

def main():
    model, bot_ismi = get_gemini_model()
    old_history = load_history()
    chat = model.start_chat(history=old_history)
    
    print(f"--- Sistem Hazır, {bot_ismi} Başlatıldı) ---")

    while True:
        user_input = input("Siz: ")
        if not user_input:
            print("Boş bir mesaj göndermezsiniz!!")
            continue
        
        if user_input.lower() in ["exit", "quit", "çıkış"]:
            save_history(chat.history)
            break
            
        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}")
        save_history(chat.history)

if __name__ == "__main__":
    main()

