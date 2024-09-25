from setuptools import setup

setup(
    name='dsa_chatbot',  
    version='0.1',
    py_modules=[
        'src.api_handler', 
        'src.dsa_module', 
        'src.sentence_builder', 
        'src.grammar_rules', 
        'src.chatbot_main'
    ],
    install_requires=[
        # Add any dependencies here
    ],
    description='A chatbot for Data Structures and Algorithms assistance',
    author='Blizzard',
    author_email='omkarmishra125@gmail.com',
    url='https://github.com/Blizzard1074/DSA-based-chatbot.git',
)
