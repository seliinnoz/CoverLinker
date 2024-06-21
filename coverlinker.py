
import os
from groq import Groq
import streamlit as st
import streamlit.components.v1 as components
from fpdf import FPDF
from streamlit_navigation_bar import st_navbar
from streamlit_option_menu import option_menu
import streamlit as st
import streamlit.components.v1 as components

# Set up Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Create Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# st.set_page_config() call must be the first command
st.set_page_config(layout="wide")

# Load image
logo_image = "/Users/selinoz/Downloads/cover-letters.jpg"


def main():
    
    page = st_navbar(["Home", "Community", "About"])
   
    if page == "Home":
        st.write("")
    elif page == "Community":
        st.write("Hello! We, as 4th-year Computer Engineering students, have created a community to share our knowledge and experiences. Our aim is to learn together, support each other, and grow together.   \n" 
                "Our Mission: To develop our knowledge and skills in computer science and achieve success together.   \n"
                "Rules and Behavioral Standards: Respect, tolerance, and open communication are prioritized in our community. It is important for participants to help each other and create a positive environment.   \n"
                "Encouragement to Participate: We encourage everyone to join our community and share their ideas. Participants at all levels are welcome!   \n"
                "Events and News: Stay tuned.   \n"
                "Contact Information: We currently wish to remain anonymous.!   \n")
        
    elif page == "About":
        st.write("Hello! We are 4th-year Computer Engineering students who have created this website to develop ourselves and promote knowledge sharing.   \n"
                "Our Story: As a team of two, we came together with a desire to share our passion for computer science. We created this platform to learn together and support each other.   \n"  
                "Mission and Vision: Our mission is to promote knowledge sharing and make computer science knowledge more accessible. Our vision is to grow together by sharing knowledge and experiences.   \n"
                "Our Team: We currently wish to remain anonymous. 👩🏻‍💻🧑🏻‍💻")






    
    # Define a session state variable
    if 'show_about_message' not in st.session_state:
        st.session_state.show_about_message = False



    image_slideshow()



    st.markdown("""
    <style>
        /* Streamlit default header and footer hidden */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Custom header style */
        .custom-header {
            position: fixed;
            top: 1;
            left: 0;
            width: 100%;
            background-color: white; /* Change background color to white */
            padding: 70px;
            display: flex;
            align-items: center; /* Align items to the center vertically */
            z-index: 1000;
        }

                
        .custom-header img {
            height: 70px; /* Adjust the logo height as needed */
        }

                
        .custom-header button {
            background-color: transparent;
            border: none;
            font-size: 16px;
            cursor: pointer;
            color: black; /* Change button text color to black */
        }

                
        .custom-header button:hover {
            text-decoration: underline;
        }

                
        /* Content margin to make space for fixed header */
        .content {
            margin-top: 70px;
            text-align: center;
        }

                
        /* Card styles */
        .card {
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 12px #aaa;
            transition: transform 0.2s, box-shadow 0.2s;
            width: 30%;
            margin: 10px;
        }
                
        .card:hover {
            transform: scale(1.05);
            box-shadow: 2px 2px 20px #888;
            background-color: #f0f0f0;
        }
                

        .navbar {
        background-color: red; /* Arka plan rengini değiştirin */
        padding: 10px;
    }
    </style>

                
   <div class="custom-header">
      <img src="./images/logo.png" alt="" border="0"  height="900" width="400">
    </div>
    """, unsafe_allow_html=True)



    # Welcome mesajı ortada
    st.markdown("""
    <div style="text-align: center; width:1500px;">
        <h1>Welcome!</h1>
        <p style="font-size:20px;">We help you create a professional and impressive cover letter.<br>
        Click the button at the bottom left to create a free cover letter.</p>
    </div>
    """, unsafe_allow_html=True)


    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    


    # If the button is clicked, set session state to show the about message
    if st.button("Create Cover Letter", key="create_cover_letter_button_main"):
        st.session_state.page = "name"
        

    st.write("""
        <style>
            div.row-widget.stButton>button {
                width: 500px;
                height: 100px; /* Adjust height as needed */
                margin: auto; /* Center align */
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Check if the about message should be shown and display it accordingly
    if st.session_state.show_about_message:
        st.write("Hello")

        


    # Boşluk ekleyerek kartları aşağıya kaydır
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)



    # Proje kartları
    col1, col2, col3 = st.columns([1, 1, 1], gap="large")  



    
    with col1:
        st.markdown("""
    <div class="card" style="margin-right: 50px;">
        <img src="./images/card1.jpg" alt="" border="0" style="width: 200px; height: 150px; margin-bottom: 10px;">
        <h2>Personalized Content</h2>
        <p>Provide your personal information, an integral part of your resume, and let our magical algorithm take care of the rest!</p>
    </div>
    """, unsafe_allow_html=True)


    with col2:
        st.markdown("""
    <div class="card" style="margin-right: 20px;">
         <img src="./images/card2.jpeg" alt="" border="0" style="width: 200px; height: 150px; margin-bottom: 10px;">
        <h2>Fast and Effective</h2>
        <p>Transform your comprehensive career experience into an impressive cover letter in no time!</p>
    </div>
    """, unsafe_allow_html=True)


    with col3:
        st.markdown("""
    <div class="card">
         <img src="./images/card3.webp" alt="" border="0" style="width: 200px; height: 150px; margin-bottom: 10px;">
        <h2>Professional Results</h2>
        <p>All the materials needed for a professional and impressive cover letter are here; just enter your information and wait!</p>
    </div>
    """, unsafe_allow_html=True)
        


            # Add custom CSS
    st.markdown("""
        <style>
        .card {
            border: 1px solid #ccc;
            padding: 100px;
            border-radius: 10px;
            box-shadow: 2px 2px 12px #aaa;
            transition: transform 0.2s, box-shadow 0.2s;
            width:350px;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 2px 2px 20px #888;
            background-color: #f0f0f0;
        }
        </style>
    """, unsafe_allow_html=True)





def image_slideshow():
    components.html(
        """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        * {box-sizing: border-box;}
        body {font-family: Verdana, sans-serif;}
        .mySlides {display: none;}
        img {vertical-align: middle;}
        
        /* Slideshow container */
        .slideshow-container {
          max-width: 1000px;
          position: relative;
          margin: auto;
        }
        
        /* Caption text */
        .text {
          color: #f2f2f2;
          font-size: 15px;
          padding: 8px 12px;
          position: absolute;
          bottom: 8px;
          width: 100%;
          text-align: center;
        }
        
        /* Number text (1/3 etc) */
        .numbertext {
          color: #f2f2f2;
          font-size: 12px;
          padding: 8px 12px;
          position: absolute;
          top: 0;
        }
        
        /* The dots/bullets/indicators */
        .dot {
          height: 15px;
          width: 15px;
          margin: 0 2px;
          background-color: #bbb;
          border-radius: 50%;
          display: inline-block;
          transition: background-color 0.6s ease;
        }
        
        .active {
          background-color: #717171;
        }
        
        /* Kapsayıcı div için stil */
        .mySlides {
            width: 550px; /* Genişliği yüzde 100 yapar (ekran boyunca) */
            height: auto;
            position: relative;
            margin: auto;
        }

        /* Resim için stil */
        .mySlides img {
            width: 100%; /* Resmi kapsayıcı div'in genişliğine uyarlar */
            height: auto; /* Yükseklik oranını korur */
        }



        /* Fading animation */
        .fade {
          animation-name: fade;
          animation-duration: 1.5s;
        }
        
        @keyframes fade {
          from {opacity: .4} 
          to {opacity: 1}
        }
        
        /* On smaller screens, decrease text size */
        @media only screen and (max-width: 300px) {
          .        text {font-size: 11px}
        }
        </style>
                </head>
        <body>

    
        <div class="slideshow-container">
        

     <div class="mySlides fade">
        
         <img src="./images/anasayfa2.jpg" alt="20" border="0">
        
    </div> 

    <div class="mySlides fade">
     <img src="./images/anasayfa1.jpg" alt="20" border="0">
    </div>
    
    
    
    <div class="mySlides fade">
        <img src="./images/anasayfa3.jpg" alt="20" border="0">
    </div>
        
</div>
        <div style="text-align:center">
          <span class="dot"></span> 
          <span class="dot"></span> 
          <span class="dot"></span> 
        </div>
        
        <script>
        let slideIndex = 0;
        showSlides();
        
        function showSlides() {
          let i;
          let slides = document.getElementsByClassName("mySlides");
          let dots = document.getElementsByClassName("dot");
          for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
          }

          slideIndex++;
          if (slideIndex > slides.length) {slideIndex = 1}    
          for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
          }

          slides[slideIndex-1].style.display = "block";  
          dots[slideIndex-1].className += " active";
          setTimeout(showSlides, 5000); // Change image every 5 seconds
        }
        
        </script>
        
        </body>
        </html>
        """,
        height=600,
    )

# Call the main function
#main()


# Step 1: Get user's name
def get_name():
    st.title("Create Cover Letter - Step 1")
    st.markdown("### Please enter your name:")
    your_name = st.text_input("Your full name:")
    
    if st.button("Next"):
        if your_name:
            st.session_state.your_name = your_name
            st.session_state.page = "profession"
        else:
            st.warning("Please enter your name to proceed.")

    if st.button("Go Back"):
        st.session_state.page = "main"




# Step 2: Get user's profession
def get_profession():
    st.title("Create Cover Letter - Step 2")
    st.markdown("### What is your profession?")
    
    predefined_professions = [
        'Software Engineer (SWE)', 'Data Scientist', 'Product Manager', 'DevOps Engineer', 'UI/UX Designer',
        'Marketing Specialist', 'Sales Manager', 'Customer Support Representative', 'Human Resources Manager',
        'Financial Analyst', 'Graphic Designer', 'Content Writer', 'Legal Advisor', 'Project Manager', 
        'Operations Manager', 'Civil Engineer', 'Mechanical Engineer', 'Electrical Engineer', 'Chemical Engineer',
        'Biomedical Engineer', 'Architect', 'Interior Designer', 'Accountant', 'Business Analyst', 
        'Research Scientist', 'Lab Technician', 'Pharmacist', 'Nurse', 'Medical Doctor', 'Dentist', 
        'Physical Therapist', 'Teacher', 'Professor', 'Librarian', 'Social Worker', 'Psychologist', 'Counselor', 
        'Event Planner', 'Chef', 'Restaurant Manager', 'Hotel Manager', 'Travel Agent', 'Real Estate Agent', 
        'Construction Manager', 'Environmental Scientist', 'Marine Biologist', 'Software Developer', 
        'IT Support Specialist', 'Network Administrator', 'System Administrator', 'Cybersecurity Specialist'
    ]

    profession_options = [''] + predefined_professions + ['Other (write own)']
    profession = st.selectbox('Your Profession:', profession_options)
    
    custom_profession = ""

    if profession == 'Other (write own)':
        custom_profession = st.text_input("Enter your profession:")
        if custom_profession:
            st.session_state.profession = custom_profession
            st.session_state.page = "strengths"
        else:
            st.warning("Please enter your profession.")
    elif profession:
        st.session_state.profession = profession
        st.session_state.page = "strengths"
    else:
        st.warning("Please select or enter your profession to proceed.")

    if st.button("Next"):
        if profession or custom_profession:
            st.session_state.page = "strengths"
        else:
            st.warning("Please select or enter your profession to proceed.")

    if st.button("Go Back"):
        st.session_state.page = "get_name"




# Step 3: Select top 3 strengths
def get_strengths():
    st.title("Create Cover Letter - Step 3")
    st.markdown("### Select your top 3 strengths:")
    
    strengths_options = [
        'Leadership', 'Communication', 'Problem Solving', 'Teamwork', 'Creativity', 'Adaptability', 
        'Organization', 'Time Management', 'Critical Thinking', 'Decision Making', 'Empathy', 
        'Attention to Detail', 'Resilience', 'Initiative', 'Flexibility', 'Interpersonal Skills', 
        'Technical Skills', 'Analytical Thinking', 'Public Speaking', 'Negotiation', 'Conflict Resolution'
    ]
    selected_strengths = st.multiselect("Select your top 3 strengths:", strengths_options, default=[])
    
    if len(selected_strengths) == 3:
        st.session_state.strengths = selected_strengths
        if st.button("Next"):
            st.session_state.page = "prof_strengths"
    elif len(selected_strengths) > 3:
        st.warning("Please select only 3 strengths.")
    else:
        st.warning("Please select 3 strengths to proceed.")

    if st.button("Go Back"):
        st.session_state.page = "profession"

# Step 4: Select profession-related strengths
def get_profession_strengths():
    st.title("Create Cover Letter - Step 4")
    st.markdown(f"### Select your top 3 {st.session_state.profession} related strengths:")
    
    profession_strengths_options = [
    'Communication', 'Decision Making', 'Management', 'Observation', 'Problem Solving', 'Technical Skills', 
    'Analytical Thinking', 'Attention to Detail', 'Leadership', 'Teamwork', 'Creativity', 'Adaptability', 
    'Organization', 'Time Management', 'Critical Thinking', 'Empathy', 'Resilience', 'Initiative', 
    'Flexibility', 'Interpersonal Skills', 'Public Speaking', 'Negotiation', 'Conflict Resolution'
    ]
    selected_profession_strengths = st.multiselect(f"Select your top 3 {st.session_state.profession} related strengths:", profession_strengths_options, default=[])
    
    if len(selected_profession_strengths) == 3:
        st.session_state.profession_strengths = selected_profession_strengths
        if st.button("Next"):
            st.session_state.page = "experience_years"
    elif len(selected_profession_strengths) > 3:
        st.warning("Please select only 3 profession-related strengths.")
    else:
        st.warning("Please select 3 profession-related strengths to proceed.")

    if st.button("Go Back"):
        st.session_state.page = "strengths"


def get_experience_years():
    st.title("Create Cover Letter - Step 5")
    st.markdown("### How many years of experience do you have?")
    
    experience_years_options = ['Less than 1 year', '1-3 years', '3-5 years', '5-10 years', 'More than 10 years']
    
    # Initialize session state if not already done
    if 'experience_years' not in st.session_state:
        st.session_state.experience_years = None
    
    # Set a default value for selected_experience_years
    selected_experience_years = st.selectbox("Select your years of experience:", experience_years_options)
    
    # Store the selection only when "Next" is clicked
    next_clicked = st.button("Next")
    back_clicked = st.button("Go Back")
    
    if next_clicked:
        if selected_experience_years:
            st.session_state.experience_years = selected_experience_years
            st.session_state.page = "job_application_details"
        else:
            st.warning("Please select your years of experience to proceed.")
    
    if back_clicked:
        st.session_state.page = "prof_strengths"




# Step 6: Get job application details
def get_job_application_details():
    st.title("Create Cover Letter - Step 6")
    st.markdown("### Please enter the job application details:")
    
    company_name = st.text_input("Company Name:", "Google")
    
    predefined_roles = [
        'Software Engineer (SWE)', 'Data Scientist', 'Product Manager', 'DevOps Engineer', 'UI/UX Designer',
        'Marketing Specialist', 'Sales Manager', 'Customer Support Representative', 'Human Resources Manager',
        'Financial Analyst', 'Graphic Designer', 'Content Writer', 'Legal Advisor', 'Project Manager', 
        'Operations Manager', 'Civil Engineer', 'Mechanical Engineer', 'Electrical Engineer', 'Chemical Engineer',
        'Biomedical Engineer', 'Architect', 'Interior Designer', 'Accountant', 'Business Analyst', 
        'Research Scientist', 'Lab Technician', 'Pharmacist', 'Nurse', 'Medical Doctor', 'Dentist', 
        'Physical Therapist', 'Teacher', 'Professor', 'Librarian', 'Social Worker', 'Psychologist', 'Counselor', 
        'Event Planner', 'Chef', 'Restaurant Manager', 'Hotel Manager', 'Travel Agent', 'Real Estate Agent', 
        'Construction Manager', 'Environmental Scientist', 'Marine Biologist', 'Software Developer', 
        'IT Support Specialist', 'Network Administrator', 'System Administrator', 'Cybersecurity Specialist'
    ]

    position_options = [''] + predefined_roles + ['Other (write own)']
    position_title = st.selectbox('Position Title:', position_options)
    
    contact_person = st.text_input("Recipient:", "Hirey McManager")
    job_description = st.text_area("This position excites me because:", "this role will allow me to work.")

    if position_title == 'Other (write own)':
        custom_position_title = st.text_input("Enter your position title:")
    else:
        custom_position_title = None

    job_des = st.text_area("Job Description:")

    if st.button("Next"):
        if company_name and ((position_title and not custom_position_title) or (custom_position_title and not position_title)) and contact_person and job_description:
            st.session_state.company_name = company_name
            if custom_position_title:
                st.session_state.position_title = custom_position_title
            else:
                st.session_state.position_title = position_title
            st.session_state.contact_person = contact_person
            st.session_state.job_description = job_description
            st.session_state.job_des = job_des
            st.session_state.page = "generate_cover_letter"
        else:
            st.warning("Please fill in all fields to proceed.")

    if st.button("Go Back"):
        st.session_state.page = "experience_years"



# Step 7: Generate and display the cover letter
def generate_cover_letter():
    st.title("Generated Cover Letter")
    
    prompt = (
        f"Write a cover letter to {st.session_state.contact_person} "
        f"from {st.session_state.your_name} for a {st.session_state.position_title} job at "
        f"{st.session_state.company_name}. I am a {st.session_state.profession} with {st.session_state.experience_years} of experience. "
        f"My top 3 general strengths are {', '.join(st.session_state.strengths)}. "
        f"My top 3 {st.session_state.profession} related strengths are {', '.join(st.session_state.profession_strengths)}. "
        f"This position excites me because {st.session_state.job_description}."
        f"Job desciption{st.session_state.job_des}."
    )

    # Generate text using Groq API
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=st.session_state.get("model_used", "llama3-8b-8192"),
        max_tokens=int(st.session_state.get("max_tokens", "1900")),
        temperature=float(st.session_state.get("temperature", "0.99")),
        top_p=float(st.session_state.get("top_p", "1"))
    )

    text = response.choices[0].message.content

    st.subheader("Cover Letter Prompt")
    st.write(prompt)
    st.subheader("Auto-Generated Cover Letter")
    st.write(text)
    #st.download_button(label='Download Cover Letter', file_name='cover_letter.txt', data=text)
    generate_pdf(text)

    with open('cl.txt', 'a') as f:
        f.write(text)

    if st.button("Go Back"):
                st.session_state.page = "job_application_details"



def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cover Letter", ln=True, align="C")
    pdf.cell(200, 10, txt="", ln=True, align="C")
    pdf.multi_cell(0, 10, txt=text)
    pdf.output("cover_letter.pdf")

    # Oluşturulan PDF dosyasını indirme düğmesi olarak göster
    st.download_button(label='Download Cover Letter (PDF)', file_name='cover_letter.pdf', data=open("cover_letter.pdf", "rb").read(), mime="application/pdf")

# Page routing logic
def page_routing():
    if 'page' not in st.session_state:
        st.session_state.page = "main"

    if st.session_state.page == "main":
        main()
    elif st.session_state.page == "name":
        get_name()
    elif st.session_state.page == "profession":
        get_profession()
    elif st.session_state.page == "strengths":
        get_strengths()
    elif st.session_state.page == "prof_strengths":
        get_profession_strengths()
    elif st.session_state.page == "experience_years":
        get_experience_years()
    elif st.session_state.page == "job_application_details":
        get_job_application_details()
    elif st.session_state.page == "generate_cover_letter":
        generate_cover_letter()

page_routing()


