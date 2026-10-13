# Savdo Hisobi — APK (Android) va EXE (Windows) yig'ish

Ilova: qarz daftari, kapital/nolga chiqish jadvali, tezkor kalkulyator (savdoga qo'shish so'rovi bilan), kunlik/haftalik/oylik statistika. Internetsiz ishlaydi.

## APK va EXE ni tayyorlash (bepul, kompyuterga hech narsa o'rnatmasdan)
1. https://github.com saytida ro'yxatdan o'ting (bepul) va yangi **private** repository oching, masalan `savdo-hisobi`.
2. Shu papkadagi **hamma fayllarni** (`.github` papkasi ham!) repositoryga yuklang: «Add file → Upload files».
3. Repositoryda **Actions** bo'limiga kiring. Build o'zi boshlanadi (yoki «APK va Windows EXE yig'ish» → **Run workflow**). ~8–12 daqiqa.
4. Tugagach, build sahifasi pastidagi **Artifacts** dan yuklab oling:
   - `SavdoHisobi-Android-APK` → `app-debug.apk` (telefonga o'rnating: «Noma'lum manbalardan o'rnatishga» ruxsat bering)
   - `SavdoHisobi-Windows` → `SavdoHisobi-1.0.0-nsis.exe` (o'rnatuvchi) va `...-portable.exe` (o'rnatmasdan ishlaydi)

## Google Play uchun
Debug APK telefonlarga to'g'ridan-to'g'ri o'rnatish uchun yetarli. Google Play'ga qo'yish uchun imzolangan (release) AAB kerak bo'ladi — buni alohida sozlash mumkin.

## Sinab ko'rish (build'siz)
`www/index.html` ni Chrome/Edge'da oching. Telefonda ham ishlaydi.
