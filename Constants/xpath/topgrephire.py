btn_singin = '//*[contains(@class, "hero_signInButton__usnj3")]'
txt_box_email = '//*[@id="email"]'
txt_box_password = '//input[@name="password"]'
btn_login = '//button[contains(text(),"Sign In")]'
login_warning = '//p[normalize-space()="Please enter the correct login details"]'
btn_add_jobs = '//*[@id="postBtn"]'
txt_box_job_title = '//input[@id="titleInput"]'
txt_box_job_desc = '//textarea[@id="descrInput"]'
txt_box_job_loc ='//textarea[@id="locationInput"]'
txt_box_job_qualify ='//textarea[@id="qualifications"]'
txt_box_job_responsble ='//textarea[@id="responsibility"]'
drop_down_clk_emp_type = '//*[@id="empType"]'
# drop_down_emp_type= '//li[@role="option"]'
drop_down_emp_type = '//ul[@role="listbox"]'
drop_down_emp_type_contract= '//li[contains(text(), "Contract")]'
drop_down_skills = '//button[@title="Open"]'
select_skills = '//input[@id="skills-select"]'
select_skill_ada = '//*[@id="skills-select"]'
btn_create_posting = '//button[@id="postButton"]'
btn_posted_job ='//button[@id="navigateButton"]'
job_container = '//div[@id="mainContainer"]'
select_skill_arrow_button ='//button[@aria-label="Open"]'
select_python = '//div[contains(@class, "MuiAutocomplete-option") and text()= "Python"]'
# select_python= "//div[contains(@class, 'MuiAutocomplete-option') and text()='Python']"
# //*[@id="skills-select"]
# //input[@aria-activedesdcendant="skills-select-option-1"]
# robot --include sanity -d Report Tests/test.robot
Slider_initial = '//span[@class="MuiSlider-mark MuiSlider-markActive css-17lmo96" and @style="left: 0%;"]'
Slider_destination = '//span[@class="MuiSlider-mark MuiSlider-markActive css-17lmo96" and @style="left: 6.66667%; width: 13.3333%;"]'
add_quiz = '//p[contains(text(),"Add Quiz?")]'
add_assessment = '//p[contains(text(),"Add Live Assessment?")]'
add_quiz_confirm = '//button[@id="confirmbutton"]'
# SSS="//div[contains(@class, 'MuiChip-label') and text()='Python']"

Job_post_alert='//div[@role="alert"]'
Close_job_post_alert = "//button[@title='Close']//*[name()='svg']"