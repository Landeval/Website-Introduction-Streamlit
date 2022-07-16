from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()
	
# Use Local CSS
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		
local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_jdeqicuf.json")
img_skate = Image.open("images/skate.jpg")
img_cyber = Image.open("images/cyber.jpg")

# ---- HEADER SECTION ----
with st.container():
	st.subheader("Hi, I am Landeval :wave:")
	st.title("A Cyber Security Expert From Indonesia")
	st.write("I am passionate about Linux and problem solving to be more effective and efficient in social life.")
	st.write("[Learn More >](https://pythonandvba.com )")
	
# ---- WHAT I DO ----
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("What I do")
		st.write("##")
		st.write(
		"""
		On my life I am hobby to research about everything. There is what i do:
		- Research about Gentleman
		- Study about Cyber Security
		- Study about Linux+
		- Study about Psychology
		- I am True Detective
		
		If this sounds interesting to you, dont worry to talk with me if you have problem. 
		Maybe I can help you to solve that!
		"""
		)
		st.write("[Youtube Channel >](https://youtube.com/channel/UCHCykZaIWieMtFH6BX1WiEw)")
	with right_column:
		st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
	st.write("---")
	st.header("My Projects")
	st.write("##")
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st.image(img_skate)
	with text_column:
		st.subheader("I Love To Play Skateboard")
		st.write(
		"""
		Skateboard is risky sport. But this is really fun and I create one video about playing skate.
		"""
		)
		st.markdown("[Watch Video...](https://youtu.be/4XNFknRr3zc)")
with st.container():
	image_column, text_column = st.columns((1, 2))
	with image_column:
		st.image(img_cyber)
	with text_column:
		st.subheader("How To Hack Like An Expert")
		st.write(
		"""
		This video will be dangerous if you misuse it for evil purposes. But it would be very helpful if you could use it for good.
		"""
		)
		st.markdown("[Watch Video...](https://youtu.be/Y7HzbRcTACo)")

# ---- CONTACT ----
with st.container():
	st.write("---")
	st.header("Get In Touch With Me!")
	st. write("##")
	
	# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
	contact_form = """
		<form action="https://formsubmit.co/kautsarputra57@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" requred></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
	st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
	st.empty()
