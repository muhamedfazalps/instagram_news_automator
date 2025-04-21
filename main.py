from news.fetcher import fetch_all_headlines
from image.generator import generate_ai_image
from instagram.uploader import post_to_instagram, verify_credentials
import pyautogui

def choose_mode():
    response = pyautogui.confirm("Choose posting mode:", buttons=["Auto", "Manual"])
    return response.lower() if response else "manual"

def prepare_caption(title):
    tags = ["#dailynews", "#india", "#instanews", "#breaking"]
    return f"📰 {title}\n\n" + " ".join(tags)

def process_news(auto_mode=True):
    headlines = fetch_all_headlines(limit=3)
    if not headlines:
        return
    for idx, headline in enumerate(headlines, 1):
        img_path = generate_ai_image(headline, idx)
        caption = prepare_caption(headline)
        if auto_mode:
            post_to_instagram(img_path, caption)
        else:
            pyautogui.alert(f"Ready to post manually: {img_path}\n\n{caption}")

def main():
    if not verify_credentials():
        return
    auto_mode = choose_mode() == "auto"
    process_news(auto_mode)

if __name__ == "__main__":
    main()
