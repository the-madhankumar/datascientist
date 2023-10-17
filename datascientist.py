import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_icon=":book:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("business website")
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["homepage","createmodel","datavisual","mail","stockdashboard","tableau","todo"],
        icons = ["book","back","clipboard-data-fill","envelope-at-fill","body-text","bar-chart","book"],
        menu_icon="cast",
    )

if selected ==  "homepage":
    import streamlit as st
    import json
    import requests
    from streamlit_lottie import st_lottie

    def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

    lottie_computer = load_lottieurl("https://lottie.host/da83f0ff-a69b-40c4-8691-8297ac96bdf1/j39KODV24b.json")

    st_lottie(lottie_computer)


    st.subheader("AutoStreamML - Your Automated Machine Learning Solution")
    st.write("""
        Welcome to AutoStreamML, your one-stop solution for automating the machine learning pipeline. This user-friendly application is powered by Streamlit, Pandas Profiling, and Pycaret, offering a seamless and efficient way to analyze data, build models, and save them for future use.""")

    st.subheader("Key Features:")

    st.subheader("Data Upload:") 
    st.write("""Begin your machine learning journey by selecting "Upload." You can easily upload your dataset, making it ready for analysis and modeling.""")

    st.subheader("Automated EDA (Exploratory Data Analysis):") 
    st.write("""Choose "Profiling" to generate automated exploratory data analysis reports. Gain valuable insights into your dataset quickly and effortlessly.""")

    st.subheader("Machine Learning Made Simple:") 
    st.write("""Dive into the world of machine learning with the "Modelling" option. Select your target variable, train models, and compare their performance with a single click. AutoStreamML streamlines the entire process, making machine learning accessible to all.""")

    st.subheader("Effortless Model Download:") 
    st.write("""Once you've trained your models, use the "Download" option to save the best-performing model as "trained_model.pkl." This model is ready for deployment and further analysis.""")


    lottie_visual = load_lottieurl("https://lottie.host/f1568a9a-f929-4842-8b6c-3218546acff5/tSw6H4MsWe.json")
    st_lottie(lottie_visual)

    st.subheader("Excel Plotter - Visualize Your Data with Ease")
    st.write("""
        Introducing the Excel Plotter, a versatile data visualization tool that empowers you to explore and visualize your Excel data effortlessly. This Streamlit-powered application simplifies the process of creating insightful charts and graphs from your Excel files.""")

    st.subheader("Key Features:")

    st.subheader("Data Grouping:") 
    st.write(""" If you have multiple columns, you can group your data by selecting the columns of interest. This feature simplifies the process of analyzing grouped data.""")

    st.subheader("Interactive Charts:") 
    st.write("""The charts are interactive and responsive. You can zoom in, pan, and hover over data points to explore your information in detail.""")

    st.subheader("Download Your Visualizations: ") 
    st.write("""Excel Plotter offers easy download options. You can download your visualizations as Excel files or HTML documents for sharing and further analysis.""")


    lottie_tableau = load_lottieurl("https://lottie.host/4be4bc84-61cc-4dbd-9640-5c8a7a98727f/jNeAIyVpY7.json")

    st_lottie(lottie_tableau)

    st.subheader("PyGWalker - Your Data Visualization Wizard")
    st.write("""
        Welcome to PyGWalker, your trusted companion for effortlessly visualizing data in a way that suits your needs. This Streamlit-powered application is designed to simplify the process of creating stunning data visualizations from your XLSX or CSV files.""")

    st.subheader("Key Features:")

    st.subheader("File Selection:") 
    st.write(""" Get started by selecting the data file you want to visualize. PyGWalker supports both XLSX and CSV file formats, ensuring flexibility with your data sources.""")

    st.subheader("Visualize Your Data:") 
    st.write(""" Once your file is uploaded, PyGWalker instantly loads your data and prepares it for visualization. You can now explore and understand your data visually.""")

    st.subheader("Chart Selection: ") 
    st.write("""PyGWalker offers a selection of charts to choose from. Whether you're looking for bar charts, line plots, scatter plots, or other chart types, you have the flexibility to pick the one that best represents your data.""")

    st.subheader("Customization: ") 
    st.write("""Customize your charts further by adjusting settings and configurations to meet your specific requirements. PyGWalker puts you in control of how your data is presented.""")


    lottie_stock = load_lottieurl("https://lottie.host/5f280b2b-be0c-4cca-a535-c0bbe3bdb0e9/AixqbYSEgX.json")

    st_lottie(lottie_stock)

    st.subheader("Stock Dashboard - Visualize Stock Data with Ease")
    st.write("""The Stock Dashboard is your all-in-one tool for gaining insights into stock market data effortlessly. Powered by Streamlit and various data sources, this application simplifies the process of tracking stock prices, analyzing performance, and staying updated with the latest news.""")

    st.subheader("Key Features:")

    st.subheader("Customized Stock Analysis:") 
    st.write(""" Begin by entering the stock ticker of your choice. The Stock Dashboard allows you to specify the start and end dates for your analysis, providing flexibility in data selection.""")

    st.subheader("Interactive Price Chart: ") 
    st.write(""" The application fetches historical stock price data and displays it using an interactive line chart. You can zoom in, pan, and hover over data points to examine stock performance over time.""")
    st.subheader("Multi-tab Interface:  ") 
    st.write("""The Stock Dashboard offers three tabs for a comprehensive analysis:\n
Pricing Data:\n
Dive into stock pricing details, including daily closing prices and percentage changes. Analyze annual returns, standard deviation, and risk-adjusted returns.\n
Fundamental Data:\n
Explore fundamental financial data, including balance sheets, income statements, and cash flow statements. Gain insights into the company's financial health.\n
Top 10 News:\n
Stay informed with the latest news related to the selected stock. The news section provides a summary, sentiment analysis, and publication details.""")


    lottie_mail = load_lottieurl("https://lottie.host/a5dc2b7b-f432-4f9b-bd32-33ef7db199b0/78ElTsPjqe.json")

    st_lottie(lottie_mail)

    st.subheader("Email Sender Web Application")
    st.write("""The "Email Sender Web Application" simplifies the process of sending emails via Gmail, offering these four key features:""")

    st.subheader("Key Features:")

    st.subheader("User-Friendly Interface:") 
    st.write("""The application boasts an intuitive and easy-to-use interface, making it accessible to users of all technical levels.""")

    st.subheader("Secure Login:") 
    st.write(""" Users provide their Gmail email address and securely input their password (masked) for authentication.""")

    st.subheader("Compose and Send Emails:") 
    st.write("""Users can compose emails by specifying the recipient's email address, subject, and email content in the provided fields.""")

    st.subheader(" Error Handling and Audio Feedback: ") 
    st.write("""The application includes robust error handling:
It prompts users to complete all required fields if left empty.\n
It checks for an internet connection and informs users to connect if needed.\n
In case of incorrect Gmail credentials, it displays an error message.\n
It provides audio feedback using text-to-speech technology, announcing "Email sent successfully" when an email is sent without errors and vocalizing error messages for user understanding.""")
    
    lottie_todo = load_lottieurl("https://lottie.host/1e08a69f-b3f0-410a-ac06-de3be282dad3/Mved1kz8yW.json")

    st_lottie(lottie_todo)
    st.subheader("Streamlit ToDo List Web Application")
    st.write("""Welcome to the Streamlit ToDo List Web Application! This user-friendly app is designed to help you manage your tasks efficiently. Whether you need to create, read, update, or delete tasks, this app has got you covered.""")

    st.subheader("Key Features:")

    st.subheader("1. Create Tasks") 
    st.write("""Easily add new tasks with details like task name, status (ToDo, Doing, Done), and due date.
Click the "Add Task" button to include your task in the list.""")

    st.subheader("2. Read Tasks") 
    st.write(""" View all your tasks at a glance.
Check the status of each task and its due date.
Get insights into task statuses using interactive pie charts.""")

    st.subheader("3. Update Tasks") 
    st.write("""Edit and update task details whenever needed.
Select the task you want to edit from the list.
Modify the task name, status, or due date, and click "Update Task.""")
    
    st.subheader("3. Update Tasks") 
    st.write("""Edit and update task details whenever needed.
Select the task you want to edit from the list.
Modify the task name, status, or due date, and click "Update Task.""")
    
    st.subheader("4. Delete Tasks") 
    st.write("""Easily remove tasks that are no longer relevant.
Select the task you want to delete from the list and click the "Delete" button.""")
    
    st.subheader("5. About") 
    st.write("""Learn more about this ToDo List App.
Built with Streamlit by Jesse E. Agbe (JCharisTech).
Powered by Streamlit Components and SQLite for data storage.""")

    

            

if selected == "createmodel":
        import streamlit as st
        import pandas as pd
        import os 
        import pandas_profiling
        from streamlit_pandas_profiling import st_profile_report
        from pycaret.regression import setup, compare_models, pull, save_model

        computer = load_lottieurl("https://lottie.host/a534da78-b648-4522-9afa-589ffc1caff8/h96cwirr21.json")

        st_lottie(computer)

        with st.sidebar:
            st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
            st.title("AutoStreamML")
            choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
            st.info("This application allows you to build an automated ML pipeline using streamlit, Pandas Profiling and Pycaret. And it damnright magic")
        if os.path.exists("sourcedata.csv"):
            df = pd.read_csv("sourcedata.csv", index_col=None)

        if choice == "Upload":
            st.title("Upload Your Data for Modelling")
            file = st.file_uploader("Upload Your Dataset HERE")
            if file:
                df = pd.read_csv(file, index_col = None)
                df.to_csv("sourcedata.csv", index = None)
                st.dataframe(df)

        if choice == "Profiling":
            st.title("Automated Exploratory Data Analysis")
            profile_report = df.profile_report()
            st_profile_report(profile_report)

        if choice == "Modelling":
            st.subheader("IN PROGRESS")
            

        if choice == "Download":
            with open("best_model.pkl", "rb") as f:
                st.download_button("Download the model", f, "trained_model.pkl")



if selected == "datavisual":
    import streamlit as st  # pip install streamlit
    import pandas as pd  # pip install pandas
    import plotly.express as px  # pip install plotly-express
    import base64  # Standard Python Module
    from io import StringIO, BytesIO  # Standard Python Module

    visual = load_lottieurl("https://lottie.host/e2ad82b5-c5eb-48d6-9e83-59ed32d991d6/uhgT0qz7DM.json")

    st_lottie(visual)

    def generate_excel_download_link(df):
        # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
        towrite = BytesIO()
        df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
        towrite.seek(0)  # reset pointer
        b64 = base64.b64encode(towrite.read()).decode()
        href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
        return st.markdown(href, unsafe_allow_html=True)

    def generate_html_download_link(fig):
        # Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
        towrite = StringIO()
        fig.write_html(towrite, include_plotlyjs="cdn")
        towrite = BytesIO(towrite.getvalue().encode())
        b64 = base64.b64encode(towrite.read()).decode()
        href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="plot.html">Download Plot</a>'
        return st.markdown(href, unsafe_allow_html=True)


    
    st.title('Excel Plotter 📈')
    st.subheader('Feed me with your Excel file')

    import pandas as pd
    import streamlit as st

    uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
    if uploaded_file:
        st.markdown('---')
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        st.dataframe(df)
        column_names = df.columns.tolist()

        # Allow user to select columns
        groupby_columns = st.multiselect("Select columns for grouping", column_names)
        if groupby_columns:
            # -- GROUP DATAFRAME
            output_columns = ['Sales', 'Profit']
            df_grouped = df.groupby(by=groupby_columns, as_index=False)[output_columns].sum()
            st.write("Grouped DataFrame:")
            st.dataframe(df_grouped)

            choice = st.selectbox("SELECT CHART YOU WANT......", ["FUNNEL","SCATTER","PIE", "BAR"]) 
            if choice is not None:
                if choice == "FUNNEL":
                    # -- PLOT FUNNEL
                    fig = px.funnel(df, x="Sales", y="Profit")
                    st.plotly_chart(fig)
                
                if choice == "SCATTER":    
                    # -- PLOT SCATTER
                    fig = px.scatter(
                        df_grouped,
                        x=groupby_columns,
                        y='Sales',
                        color='Profit',
                        color_continuous_scale=['red', 'yellow', 'green'],
                        template='plotly_white',
                        title=f'<b>Sales & Profit by {groupby_columns}</b>'
                    )
                    st.plotly_chart(fig)
                
                if choice == "PIE":      
                    # -- PLOT BAR
                    fig = px.pie(
                        df_grouped,
                        values='Sales',
                        color='Profit',
                        template='plotly_white',
                        title=f'<b>Sales & Profit by {groupby_columns}</b>'
                    )
                    st.plotly_chart(fig)
                
                if choice == "BAR":      
                    # -- PLOT BAR
                    fig = px.bar(
                        df_grouped,
                        x=groupby_columns,
                        y='Sales',
                        color='Profit',
                        color_continuous_scale=['red', 'yellow', 'green'],
                        template='plotly_white',
                        title=f'<b>Sales & Profit by {groupby_columns}</b>'
                    )
                    st.plotly_chart(fig)

                # -- DOWNLOAD SECTION
                st.subheader('Downloads:')
                generate_excel_download_link(df_grouped)
                generate_html_download_link(fig)
                st.info("Task completed!!!!")
            else:
                st.error("Could you please select the column for the grouping")




if selected == "tableau":
    import streamlit as st
    import pandas as pd
    import pygwalker as pyg

    tableau = load_lottieurl("https://lottie.host/3591b49e-3ae2-4137-945a-d741f9064a49/c8HNZeYMZB.json")

    st_lottie(tableau)
    

    st.title('tableau')
    choice = st.selectbox("SELECT CHART YOU WANT......", ["XLSX","CSV"])
    if choice == "XLSX":
        uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
        if uploaded_file is None:
            st.error("please select a dataset....")
        else:
            df = pd.read_excel(uploaded_file)
            pyg.walk(df, env='Streamlit', dark='dark')
    if choice == "CSV":
        uploaded_file = st.file_uploader('Choose a XLSX file', type='csv')
        if uploaded_file is None:
            st.error("please select a dataset....")
        else:
            df = pd.read_csv(uploaded_file)
            pyg.walk(df, env='Streamlit', dark='dark')



if selected == "stockdashboard":
    import streamlit as st, pandas as pd, numpy as np, yfinance as yf
    import plotly.express as px

    stock = load_lottieurl("https://lottie.host/012d3055-a168-463a-8bbf-7236e6319768/UTNFd4Xl1P.json")

    st_lottie(stock)

    st.title("Stock Dashboard")
    ticker = st.sidebar.text_input("Ticker")
    start_date = st.sidebar.date_input("Start Date")
    end_date = st.sidebar.date_input("End Date")

    data = yf.download(ticker,start = start_date, end = end_date)
    fig = px.line(data, x = data.index, y = data["Adj Close"], title = ticker)
    st.plotly_chart(fig)

    pricing_data, fundamental_data, news = st.tabs(["Pricing Data","Fundamental Data", "Top 10 News"])

    with pricing_data:
        st.write("Price")
        data2 = data
        data2["% Change"] = data["Adj Close"]/data["Adj Close"].shift(1) - 1
        data2.dropna(inplace = True)
        st.write(data)
        annual_return = data2["% Change"].mean()*252*100
        st.write("Annual Return is ",annual_return,"%")
        stdev = np.std(data2["% Change"])*np.sqrt(252)
        st.write("Standard Deviation is ", stdev*100,"%")
        st.write("Risk Adj, Return is ",annual_return/(stdev*100))

    from alpha_vantage.fundamentaldata import FundamentalData
    with fundamental_data:
        key = "9Z1Z01K4E1DNN1AI"
        fd = FundamentalData(key, output_format = "pandas")
        st.subheader("Balance Sheet")
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
        st.subheader("Income Statement")
        income_statement = fd.get_income_statement_annual(ticker)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)
        st.subheader("Cash Flow Statement")
        cash_flow = fd.get_cash_flow_annual(ticker)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf)

    from stocknews import StockNews
    with news:
        st.header(f"News of {ticker}")
        sn = StockNews(ticker, save_news = False)
        df_news = sn.read_rss()
        for i in range(10):
            st.write(df_news["published"][i])
            st.write(df_news["title"][i])
            st.write(df_news["summary"][i])
            title_sentiment = df_news["sentiment_title"][i]
            st.write(f"Title Sentiment {title_sentiment}")
            news_sentiment = df_news["sentiment_summary"][i]
            st.write(f"News Sentiment {news_sentiment}")

if selected == "mail":
    import streamlit as st
    import smtplib as s
    import os
    from PIL import Image
    import pythoncom  # Import the pythoncom module for COM initialization
    from win32com.client import Dispatch

    mail = load_lottieurl("https://lottie.host/ea8c94d5-74d0-4614-ab7c-36d9d8e9e682/Qz9gcbd1aP.json")

    st_lottie(mail)
    def speak(str):
        pythoncom.CoInitialize()  # Initialize COM
        try:
            speak = Dispatch("SAPI.SpVoice")
            speak.Speak(str)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            pythoncom.CoUninitialize()  # Uninitialize COM

    def main():
        st.title("Email Sender Web application")
        email_sender = st.text_input("Enter User Email - ")
        password = st.text_input("Enter User password - ", type="password")
        email_receiver = st.text_input("Enter Receiver Email = ")
        subject = st.text_input("Your Email Subject - ")
        body = st.text_area("Your Email:")
        if st.button("Send Email"):
            try:
                connection = s.SMTP("smtp.gmail.com", 587)
                connection.starttls()
                connection.login(email_sender, password)
                message = "Subject:{}\n\n{}".format(subject, body)
                connection.sendmail(email_sender, email_receiver, message)
                connection.quit()
                st.success("Email sent Successfully.")
                speak("Email sent Successfully")
            except Exception as e:
                if email_sender == "":
                    st.error("Please Fill User Email Field")
                    speak("Please Fill User Email Field")
                elif password == "":
                    st.error("Please Fill User password Field")
                    speak("Please Fill User password Field")
                elif email_receiver == "":
                    st.error("Please Fill Receiver Email Field")
                    speak("Please Fill Receiver Email Field")
                else:
                    a = os.system("ping www.google.com")
                    if a == 1:
                        st.error("Please Connect Your Internet Connection")
                        speak("Please Connect Your Internet Connection")
                    else:
                        st.error(f"Wrong Email or Password.!{e}")
                        speak("Wrong Email or Password")

    if __name__ == "__main__":
        main()


if selected == "todo":
    import streamlit as st
    import pandas as pd 
    import streamlit.components.v1 as stc
    import sqlite3
    
    
    conn = sqlite3.connect('data.db',check_same_thread=False)
    c = conn.cursor()


    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT,task_due_date DATE)')


    def add_data(task,task_status,task_due_date):
        c.execute('INSERT INTO taskstable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
        conn.commit()


    def view_all_data():
        c.execute('SELECT * FROM taskstable')
        data = c.fetchall()
        return data

    def view_all_task_names():
        c.execute('SELECT DISTINCT task FROM taskstable')
        data = c.fetchall()
        return data

    def get_task(task):
        c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
        data = c.fetchall()
        return data

    def get_task_by_status(task_status):
        c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
        data = c.fetchall()


    def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
        c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
        conn.commit()
        data = c.fetchall()
        return data

    def delete_data(task):
        c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
        conn.commit()


    # Data Viz Pkgs
    import plotly.express as px 
    todo = load_lottieurl("https://lottie.host/213a4afa-db60-4d8a-bf8b-066a787718e6/4p2ujfhjsC.json")

    st_lottie(todo)

    def main():


        menu = ["Create","Read","Update","Delete"]
        choice = st.sidebar.selectbox("Menu",menu)
        create_table()

        if choice == "Create":
            st.subheader("Add Item")
            col1,col2 = st.columns(2)
            
            with col1:
                task = st.text_area("Task To Do")

            with col2:
                task_status = st.selectbox("Status",["ToDo","Doing","Done"])
                task_due_date = st.date_input("Due Date")

            if st.button("Add Task"):
                add_data(task,task_status,task_due_date)
                st.success("Added ::{} ::To Task".format(task))


        elif choice == "Read":
            # st.subheader("View Items")
            with st.expander("View All"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                st.dataframe(clean_df)

            with st.expander("Task Status"):
                task_df = clean_df['Status'].value_counts().to_frame()
                # st.dataframe(task_df)
                task_df = task_df.reset_index()
                st.dataframe(task_df)

                p1 = px.pie(task_df,names='index',values='Status')
                st.plotly_chart(p1,use_container_width=True)


        elif choice == "Update":
            st.subheader("Edit Items")
            with st.expander("Current Data"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                st.dataframe(clean_df)

            list_of_tasks = [i[0] for i in view_all_task_names()]
            selected_task = st.selectbox("Task",list_of_tasks)
            task_result = get_task(selected_task)
            # st.write(task_result)

            if task_result:
                task = task_result[0][0]
                task_status = task_result[0][1]
                task_due_date = task_result[0][2]

                col1,col2 = st.columns(2)
                
                with col1:
                    new_task = st.text_area("Task To Do",task)

                with col2:
                    new_task_status = st.selectbox(task_status,["ToDo","Doing","Done"])
                    new_task_due_date = st.date_input(task_due_date)

                if st.button("Update Task"):
                    edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
                    st.success("Updated ::{} ::To {}".format(task,new_task))

                with st.expander("View Updated Data"):
                    result = view_all_data()
                    # st.write(result)
                    clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                    st.dataframe(clean_df)


        elif choice == "Delete":
            st.subheader("Delete")
            with st.expander("View Data"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                st.dataframe(clean_df)

            unique_list = [i[0] for i in view_all_task_names()]
            delete_by_task_name =  st.selectbox("Select Task",unique_list)
            if st.button("Delete"):
                delete_data(delete_by_task_name)
                st.warning("Deleted: '{}'".format(delete_by_task_name))

            with st.expander("Updated Data"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result,columns=["Task","Status","Date"])
                st.dataframe(clean_df)


    if __name__ == '__main__':
        main()

