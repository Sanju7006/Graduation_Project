import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return None

def generate_summary(transcript_text):
    parser = PlaintextParser.from_string(transcript_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 10)  # Summarize to 10 sentences
    summary_text = " ".join(str(sentence) for sentence in summary)
    return summary_text

def format_summary(title, summary_text):
    # Create bullet points from summary text
    bullet_points = "\n".join(f"- {sentence.strip()}" for sentence in summary_text.split('.') if sentence.strip())

    # Create conclusion
    conclusion = "This concludes the summary of the video."

    # Combine title, bullet points, and conclusion
    formatted_summary = f"**Title:** {title}\n\n**Bullet Points:**\n{bullet_points}\n\n**Conclusion:** {conclusion}"
    return formatted_summary

# Streamlit app
st.write('<p style="color: red; font-weight: bold; text-align: justify;">Video</p>', unsafe_allow_html=True)
st.write('YouTube video summarizer')

# Input fields for video title and link
title = st.text_input('Enter the title of the YouTube video:')
link = st.text_input('Enter the link of the YouTube video you want to summarize:')

if st.button('Start'):
    if title and link:
        try:
            video_id = link.split("v=")[-1]
            progress = st.progress(0)
            status_text = st.empty()
            status_text.text('Loading the transcript...')
            progress.progress(25)

            transcript_text = get_transcript(video_id)

            if transcript_text:
                status_text.text('Creating summary...')
                progress.progress(75)

                summary_text = generate_summary(transcript_text)

                # Format the summary with the title
                formatted_summary = format_summary(title, summary_text)

                status_text.text('Summary:')
                st.markdown(formatted_summary, unsafe_allow_html=True)

                progress.progress(100)
                status_text.text('Process completed successfully.')
            else:
                st.write('Could not retrieve transcript. Please check the video link.')
        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write('Please enter both the title and a valid YouTube link.')
