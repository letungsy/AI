import streamlit as st
import os
# import playsound
# import speech_recognition as sr
import time
# import wikipedia
import datetime
import webbrowser
import requests
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
# from gtts import gTTS
from youtube_search import YoutubeSearch

# Khai báo các biến cho quá trình làm trợ lý ảo
# wikipedia.set_lang('vi')
# language = 'vi'
# path = ChromeDriverManager().install()

# Text - to - speech: Chuyển đổi văn bản thành giọng nói
# def speak(text):
#     tts = gTTS(text=text, lang=language, slow=False)
#     tts.save("sound.mp3")
#     playsound.playsound("sound.mp3", False)
#     os.remove("sound.mp3")

# Streamlit interface
st.title("Trợ Lý Ảo Của SY PRO")
st.write("Xin chào! Tôi là matinh, trợ lý ảo của bạn. Hãy nhập lệnh bạn muốn tôi thực hiện:")

def assistant():
    st.write("Xin chào, bạn tên là gì nhỉ?")
    name = st.text_input("Tên của bạn là gì?")
    if name:
        st.write(f"Chào bạn {name}")
        st.write("Bạn cần Bot matinh có thể giúp gì ạ?")
        st.write("""Bot chỉ giúp bạn khi bạn nhập đúng câu lệnh sau vào khung nhập lệnh của bạn\n
                 1.chào\n
                 2.giờ
                 3.ngày
                 4.thời tiết
                 5.chơi nhạc
                 6.mở google và tìm kiếm
                 7.bách khoa toàn thư
                 8.giới thiệu""")
        command = st.text_input("Nhập lệnh của bạn:")
        if command:
            if "dừng" in command or "tạm biệt" in command or "chào robot" in command or "ngủ thôi" in command:
                st.write("Hẹn gặp lại bạn sau!")
            elif "có thể làm gì" in command:
                help_me()
            elif "chào" in command:
                hello(name)
            elif "giờ" in command or "ngày" in command:
                get_time(command)
            # elif 'mở google và tìm kiếm' in command:
            #     open_google_and_search(command)
            elif "thời tiết" in command:
                current_weather()
            elif "chơi nhạc" in command:
                play_song()     
            elif "bách khoa toàn thư" in command:
                tell_me_about()
            elif "giới thiệu" in command:
                introduce()

def help_me():
    st.write("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi\n
    2. Hiển thị giờ\n
    3. Hiển thị ngày\n
    4. Tìm kiếm trên Google\n
    5. Dự báo thời tiết\n
    6. Mở video nhạc\n
    7. Kể bạn biết về thế giới """)

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak(f"Chào buổi sáng bạn {name}. Chúc bạn một ngày tốt lành.")
    elif 12 <= day_time < 18:
        st.write(f"Chào buổi chiều bạn {name}. Bạn đã dự định gì cho chiều nay chưa.")
    else:
        st.write(f"Chào buổi tối bạn {name}. Bạn đã ăn tối chưa nhỉ.")

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        st.write(f'Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây')
    elif "ngày" in text:
        st.write(f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        st.write("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")




# def open_google_and_search(text):
#     st.write('Bạn muốn tìm kiếm gì')
#     query = st.text_input("Nhập từ khóa tìm kiếm trên Google:")
#     query = query.replace('', '+')
#     if query:
#         browser = webdriver.Chrome()
#         for i in range(1):
#          e = browser.get("https://www.google.com/search?q="+ query + "&start" + str(i))
#         time.sleep(15) 
       


def current_weather():
    st.write("Bạn muốn xem thời tiết ở đâu ạ.")
    city = st.text_input("Thành phố:")
    if city:
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        ow_url = "http://api.openweathermap.org/data/2.5/weather?"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_temperature = city_res["temp"]
            current_pressure = city_res["pressure"]
            current_humidity = city_res["humidity"]
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
            wthr = data["weather"]
            weather_description = wthr[0]["description"]
            now = datetime.datetime.now()
            content = f"""
            Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
            Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
            Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
            Nhiệt độ trung bình là {current_temperature} độ C
            Áp suất không khí là {current_pressure} héc tơ Pascal
            Độ ẩm là {current_humidity}%
            Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi."""
            st.write(content)
        else:
            st.write("Không tìm thấy địa chỉ của bạn")

def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    mysong = st.text_input("Tên bài hát:")
    if mysong:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        webbrowser.open(url)
        speak("Bài hát bạn yêu cầu đã được mở.")



def tell_me_about():
    try:
        st.write("Bạn cần Bot đọc gì ạ")
        text = st.text_input("Chủ đề:")
        contents = wikipedia.summary(text).split('\n')
        st.write(contents[0])
        for content in contents[1:]:
            # speak("Bạn muốn nghe thêm không?")
            ans = st.text_input("Trả lời (có/không):")
            if 'có' not in ans:
                break
            st.write(content)
        st.write('Cảm ơn bạn đã lắng nghe!!!')
    except:
        st.write("Bot  định nghĩa được thuật ngữ của bạn. Bạn nhập vào chủ đề được không?")

def introduce():
    st.write("Xin chào mọi người. Mình là trợ lý ảo AI do LÊ TÙNG SỸ tạo ra. Mình có thể giúp bạn làm nhiều việc lắm đó. Bạn có muốn tìm hiểu không?")

if __name__ == "__main__":
    assistant()
