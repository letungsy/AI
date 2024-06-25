import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os
import pyttsx3
import speech_recognition as sr
# import time
import wikipedia
import datetime
# import webbrowser
import requests
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
# from gtts import gTTS
# from youtube_search import YoutubeSearch
load_dotenv()
API_KEY=os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)
# Khai báo các biến cho quá trình làm trợ lý ảo
wikipedia.set_lang('vi')
language = 'vi'
# path = ChromeDriverManager().install()
st.header(":mailbox: Trợ Lý Ảo Của SỸ PRO 🙉 🙁 😝")
contact_form = """
<h2>Xin chào! Tôi là matinh, trợ lý ảo của bạn. Hãy nhập lệnh bạn muốn tôi thực hiện:</h2>
<h3>Xin chào, bạn tên là gì nhỉ?</h3>
"""
st.markdown(contact_form, unsafe_allow_html=True)
# Text - to - speech: Chuyển đổi văn bản thành giọng nói
def GPT():
    # st.image("./Google_PaLM_Logo.svg.webp", use_column_width=False, width=100)
    st.header("Chat with GPT")
    st.write("")
    prompt = st.text_input("Mòi nhập",placeholder="bạn có thể nhập bất kì gì bằng tiếng anh", label_visibility="visible")
    # temp = st.slider("Temperature", 0.0, 1.0, step=0.05)    #Hyper parameter - range[0-1]
    if st.button("NHẬP VÀO", use_container_width=True):
        model = "models/text-bison-001"    #This is the only model currently available
        response = palm.generate_text(
            model=model,
            prompt=prompt,
            # temperature=temp,
            max_output_tokens=20000
        )

        st.write("")
        st.header(":blue[TRẢ LỜI]")
        st.write("")

        st.markdown(response.result, unsafe_allow_html=False, help=None)
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume - 0.0)  # tu 0.0 -> 1.0
    engine.setProperty('rate', rate - 50)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
def assistant():
    name = st.text_input("Tên bạn",placeholder="Mời bạn nhập tên:",label_visibility="visible")
    if name:
        st.write(f"Chào bạn {name}")
        st.write("Bạn cần Bot matinh có thể giúp gì ạ?")
        contact = """<h6>Bot chỉ giúp bạn khi bạn nhập đúng câu lệnh sau vào khung nhập lệnh của bạn</h6>
<h6>1.chào</h6>
<h6>2.giờ</h6>
<h6>3.ngày</h6>
<h6>4.thời tiết</h6>
<h6>5.chơi nhạc</h6>
<h6>6.mở google và tìm kiếm</h6>
<h6>7.bách khoa toàn thư</h6>
<h6>8.giới thiệu</h6>
<h6>9.có thể làm gì</h6>
<h6>10.GPT</h6>
<h6>11.dừng</h6>
<h4>Ghi chú : GPT chỉ có thể viết bằng tiếng anh,tiếng việt chưa hỗ trợ</h4>
"""
        st.markdown(contact, unsafe_allow_html=True)
        command = st.text_input("Nhập lệnh của bạn",placeholder="Nhập lệnh của bạn:",label_visibility="visible")
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
            #     # open_google_and_search(command)
            elif "thời tiết" in command:
                current_weather()
            # elif "chơi nhạc" in command:
            #     play_song()     
            elif "bách khoa toàn thư" in command:
                tell_me_about()
            elif "giới thiệu" in command:
                introduce()
            elif "GPT" in command:   
                GPT() 

def help_me():
  contact1 = """<h6>Bot có thể giúp bạn thực hiện các câu lệnh sau đây:</h6>
<h6>1.Chào hỏi</h6>
<h6>2.Hiển thị giờ</h6>
<h6>3.Hiển thị ngày</h6>
<h6>4.Tìm kiếm trên Google</h6>
<h6>5.chơi nhạc</h6>
<h6>6.Dự báo thời tiết</h6>
<h6>7.Kể bạn biết về thế giới</h6>
<h6>8.CHAT GPT</h6>
"""
  st.markdown(contact1, unsafe_allow_html=True)

def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak(f"Chào buổi sáng bạn {name}. Chúc bạn một ngày tốt lành.")
        st.write(f"Chào buổi sáng bạn {name}. Chúc bạn một ngày tốt lành.")
    elif 12 <= day_time < 18:
        speak(f"Chào buổi chiều bạn {name}. Bạn đã dự định gì cho chiều nay chưa.")
        st.write(f"Chào buổi chiều bạn {name}. Bạn đã dự định gì cho chiều nay chưa.")
    else:
        speak(f"Chào buổi tối bạn {name}. Bạn đã ăn tối chưa nhỉ.")
        st.write(f"Chào buổi tối bạn {name}. Bạn đã ăn tối chưa nhỉ.")

def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak(f'Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây')
        st.write(f'Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây')
    elif "ngày" in text:
        speak(f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
        st.write(f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
        st.write("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")

# def open_google_and_search(text):
#     speak('Bạn muốn tìm kiếm gì')
#     st.write('Bạn muốn tìm kiếm gì')
#     query = st.text_input("Nhập từ khóa",placeholder="Nhập từ khóa tìm kiếm trên Google:",label_visibility="visible")
#     query = query.replace('', '+')
#     if query:
#         browser = webdriver.Chrome()
#         for i in range(1):
#          e = browser.get("https://www.google.com/search?q="+ query + "&start" + str(i))
#         time.sleep(15) 
       

def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    st.write("Bạn muốn xem thời tiết ở đâu ạ")
    city = st.text_input("Thành phố",placeholder="Thành phố:",label_visibility="visible")
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
            speak(content)
            st.write(content)
        else:
            speak("Không tìm thấy địa chỉ của bạn")

# def play_song():
#     speak('Xin mời bạn chọn tên bài hát')
#     mysong = st.text_input("Tên bài hát",placeholder="Tên bài hát:",label_visibility="visible")
#     if mysong:
#         result = YoutubeSearch(mysong, max_results=10).to_dict()
#         url = 'https://www.youtube.com' + result[0]['url_suffix']
#         webbrowser.open(url)
#         speak("Bài hát bạn yêu cầu đã được mở.")


def tell_me_about():
    try:
        st.write("Bạn cần Bot đọc gì ạ")
        text = st.text_input("Chủ đề",placeholder="Chủ đề:",label_visibility="visible")
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        st.write(contents[0])
        for content in contents[1:]:
            # speak("Bạn muốn nghe thêm không?")
            ans = st.text_input("Trả lời",placeholder="Trả lời (có/không) bot đọc tiếp:",label_visibility="visible")
            if 'có' not in ans:
                break
            speak(content)
            st.write(content)
        speak('Cảm ơn bạn đã lắng nghe!!!')
    except:
        speak("Bot  định nghĩa được thuật ngữ của bạn. Bạn nhập vào chủ đề được không?")

def introduce():
    speak("Xin chào mọi người. Mình là trợ lý ảo AI do LÊ TÙNG SỸ tạo ra. Mình có thể giúp bạn làm nhiều việc lắm đó. Bạn có muốn tìm hiểu không?")
    st.write("Xin chào mọi người. Mình là trợ lý ảo AI do LÊ TÙNG SỸ tạo ra. Mình có thể giúp bạn làm nhiều việc lắm đó. Bạn có muốn tìm hiểu không")
if __name__ == "__main__":
    assistant()
