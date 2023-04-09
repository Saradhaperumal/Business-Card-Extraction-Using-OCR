import streamlit as st
from function import upload_database, extracted_data, show_database

# Set the page title
st.set_page_config(page_title='Business Card Information Extractor')

# Add a title to the page
st.title('Business Card Information Extractor')

# Add a file uploader to the page
image_file = st.file_uploader('Upload an image of a business card', type=['jpg', 'jpeg', 'png'])

file_name = 'Doc1'

if image_file is not None:
        with open(f'{file_name}.png', 'wb') as f:
            f.write(image_file.getvalue())

# Extracting and Uploading 
with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            b1=st.button('Extract Data ')
          
        with col2:
            b2=st.button('Upload data')
            
        with col3:
            b3=st.button('Show Data')
            
        if b1:
            extracted = extracted_data(f'{file_name}.png')
            st.image(extracted)

        #st.subheader('Upload Database')
        if b2:
            upload_database(f'{file_name}.png')
            st.success("Data Uploaded Successfully")

        df=show_database()
        if b3:
                st.dataframe(df)


       