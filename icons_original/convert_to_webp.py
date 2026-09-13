import os
import glob
from PIL import Image

def convert_all_to_webp():
    # Ищем все картинки, кроме уже готовых webp
    images = []
    for ext in ('*.png', '*.jpg', '*.jpeg'):
        images.extend(glob.glob(ext))
        
    if not images:
        print("Нет новых картинок для конвертации.")
        return

    for img_path in images:
        try:
            # Открываем картинку
            img = Image.open(img_path).convert("RGBA")
            # Делаем идеальный квадрат 160x160
            img = img.resize((160, 160), Image.Resampling.LANCZOS)
            
            # Сохраняем в WebP
            base = os.path.splitext(img_path)[0]
            img.save(f"{base}.webp", "webp", quality=85)
            
            # Удаляем исходник
            os.remove(img_path)
            print(f"✅ Сконвертировано: {base}.webp")
        except Exception as e:
            print(f"❌ Ошибка с {img_path}: {e}")

if __name__ == "__main__":
    convert_all_to_webp()
    print("🎉 Все файлы теперь в формате WebP!")