import streamlit as st
import time
from plyer import notification
import winsound  # Works on Windows for the beep

# Page Configuration
st.set_page_config(page_title="Hydration Reminder", page_icon="💧")

st.title("💧 Personalized Hydration Reminder")
st.write("Configure your settings below and click 'Start' to begin.")

# --- Sidebar / Customization Options ---
with st.sidebar:
    st.header("Settings")
    user_name = st.text_input("Your Name", value="Deepak")
    custom_message = st.text_area("Reminder Message", value="Water is essential for good health. Stay hydrated!")
    
    # Notification Frequency
    freq_unit = st.selectbox("Frequency Unit", ["Minutes", "Hours"])
    interval = st.number_input(f"Repeat every ({freq_unit})", min_value=1, value=60)
    
    # Sound Option
    sound_on = st.checkbox("Enable Beep Sound", value=True)

# Convert interval to seconds
sleep_time = interval * 60 if freq_unit == "Minutes" else interval * 3600

# --- App Logic ---
start_button = st.button("Start Reminder Loop")
stop_placeholder = st.empty()

if start_button:
    st.success(f"Reminder set for every {interval} {freq_unit.lower()}!")
    
    # This loop runs while the app is open
    while True:
        # 1. Trigger System Notification
        notification.notify(
            title=f"Drink Water, {user_name}!",
            message=custom_message,
            app_icon=None,  # You can add a path to an .ico file here
            timeout=10
        )
        
        # 2. Trigger Sound (Windows specific)
        if sound_on:
            winsound.Beep(1000, 500)  # Frequency 1000Hz, Duration 500ms
        
        # 3. Wait for the next interval
        time.sleep(sleep_time)
        
        # Streamlit rerun logic (optional)
        st.write(f"Last notified at: {time.strftime('%H:%M:%S')}")
