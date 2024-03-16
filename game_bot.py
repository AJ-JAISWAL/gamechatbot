import streamlit as st
import random

qa_pairs1 = {
    "what is game development?": "Game development is the process of creating video games. It involves designing, programming, art creation, and testing.",
    "what are the different stages of game development?":"The stages typically include concept development, pre-production, production, testing, and post-production.",
    "which programming languages are commonly used in game development?":"Common languages include C++, C#, Java, and Python.",
    "What is the role of a game designer?":"Game designers are responsible for conceptualizing game mechanics, creating level designs, and defining the overall gameplay experience.",
    "what is the difference between 2D and 3D game development?":"2D games are played on a 2-dimensional plane, while 3D games offer a more immersive experience with three-dimensional environments and characters.",
    "what software is commonly used for game development?":"Popular game development software includes Unity, Unreal Engine, Godot, and GameMaker Studio.",
    "what skills are essential for a game developer?":"Skills include programming, game design, graphic design, animation, storytelling, and problem-solving.",
    "how can I learn game development?":"You can learn game development through online tutorials, courses, books, and by practicing with game development software.",
    "what are some common pitfalls in game development?":"Common pitfalls include scope creep, poor project management, and underestimating development time and costs.",
    "what is game optimization?":"Game optimization involves improving the performance of a game by reducing resource usage and increasing frame rates.",
    "what is game monetization?":"Game monetization is the process of generating revenue from a game. This can include selling the game, in-game purchases, ads, or subscription models.",
    "how do you design engaging gameplay?":"Engaging gameplay is often achieved through a balance of challenge, reward, and player agency. Iterative testing and player feedback are essential.",
    "what is the importance of storytelling in games?":"Storytelling adds depth and context to the game world, helping players become more emotionally invested in the experience.",
    "how do you create game art?":"Game art can be created using software like Adobe Photoshop, Blender, Autodesk Maya, or by hand-drawing and scanning.",
    "what is procedural generation in games?":"Procedural generation involves using algorithms to create game content dynamically, such as levels, terrain, or textures.",
}
qa_pairs2 = {
    "what is a database in web development?":"A database is a structured collection of data. In web development, databases are used to store and manage information for dynamic websites and web applications.",
    "what is sql?":"SQL (Structured Query Language) is a standard programming language used to manage relational databases.",
    "what is nosql?":"NoSQL (Not Only SQL) is a term used to describe databases that use non-relational models. They are often used for large-scale distributed data storage.",
    "what is git?":"Git is a distributed version control system used to track changes in source code during software development.",
    "what is a repository in git?":"A repository is a storage location where Git stores files and their history.",
    "what is version control?":"Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.",
    "what is a web server?":"A web server is software that serves web pages to clients over the HTTP protocol.",
    "what is apache?":"Apache is a popular open-source web server software.",
    "what is nginx?":"Nginx is a high-performance, open-source web server software used for serving static and dynamic content on the web.",
    "what is a domain name?":"A domain name is the human-readable address of a website, such as example.com.",
    "what is dns?":"DNS (Domain Name System) is a system that translates domain names into IP addresses, allowing users to access websites using domain names.",
    "what is web hosting?":"Web hosting is a service that allows individuals and organizations to make their website accessible via the World Wide Web.",
    "what is a web browser?":"A web browser is a software application used to access information on the World Wide Web.",
    "what is a web application?":"A web application is a software application that runs on a web server and is accessed through a web browser over a network.",
    "what is http?":"HTTP (Hypertext Transfer Protocol) is the protocol used for transmitting data on the World Wide Web.",
    "what is a cookie?":"A cookie is a small piece of data sent from a website and stored on the user's computer by the web browser."
}
qa_pairs3 = {
    "what is cross-site scripting ?":"Cross-site scripting is a security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users.",
    "what is a session?":"A session is a period of time during which a user interacts with a web application.",
    "what is a web framework?":"A web framework is a software framework designed to support the development of web applications.",
    "what is a template engine?":"A template engine is a software module that generates HTML documents dynamically based on templates and data provided by the developer.",
    "what is url rewriting?":"URL rewriting is the process of modifying a URL's appearance, typically for the purpose of improving search engine optimization (SEO) or making the URL more user-friendly.",
    "what is web accessibility?":"Web accessibility refers to the inclusive practice of ensuring websites are usable by people of all abilities and disabilities.",
    "what is the difference between put and post requests?":"PUT is used to update or replace an existing resource, while POST is used to create a new resource.",
    "what is a web service?":"A web service is a software system designed to support interoperable machine-to-machine interaction over a network.",
    "what is a microservice architecture?":"Microservice architecture is an architectural style that structures an application as a collection of small, loosely coupled services.",
    "what is serverless computing?": "Serverless computing is a cloud computing execution model in which the cloud provider dynamically manages the allocation of machine resources.",
    "what is progressive web app?": "Progressive Web Apps are web applications that use modern web capabilities to provide a user experience similar to that of native apps.",
    "what is single page application (SPA)?": "A Single Page Application is a web application that interacts with the user by dynamically rewriting the current page rather than loading entire new pages from the server.",
    "what is web scraping?": "Web scraping is the process of extracting data from websites.",
    "what is a web socket?": "A web socket is a communication protocol that provides full-duplex communication channels over a single TCP connection.",
    "what is a cdn?": "A CDN (Content Delivery Network) is a distributed network of servers that delivers web content to users based on their geographic location.",
    "what is a framework in javascript?": "A JavaScript framework is a pre-written JavaScript code library that makes it easier for developers to build dynamic web pages and web applications.",
    "what is the difference between synchronous and asynchronous programming?": "In synchronous programming, operations block until the task is completed, while in asynchronous programming, operations can continue while waiting for a task to complete.",
    "what is web performance optimization?": "Web performance optimization is the process of improving the speed and efficiency of a website or web application."
}

pairs = [qa_pairs1, qa_pairs2, qa_pairs3]
random_pair = qa_pairs1

def respond_to_question(question):
    if question in random_pair:
        return random_pair[question]
    else:
        return "Enter Wrong Information! Please Check The Query?"
st.set_page_config(page_title="😎🧠 Game Developer Chatbot")

with st.sidebar:
    st.title('😎🧠 Game Developer Chatbot')
    st.write('This chatbot will provide the knowledge about Game Development.')
    st.write("Today questions task to learn.")
    for i in random_pair:
        st.write(i)

st.title("Game Developer ChatBot")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How May I Help You Today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "How May I Help You Today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history())

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = respond_to_question(prompt.lower())
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

