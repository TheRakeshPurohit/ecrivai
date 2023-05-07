from langchain.prompts import PromptTemplate


keyword_prompt = PromptTemplate(
        input_variables=["topic"],
        template="Give me a list of 5 keywords that for using in blog about {topic}",
    )

content_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""Write a blog post about: {topic}. The blog post should have the following characteristics:
- The style and tone of the blog should be informative. You should write in the first person and use a friendly and engaging voice.
- The length of the blog post should be around 600 words.
- The blog must contain these sections: introduction, body, and conclusion.
- Each section should have a clear and catchy heading that summarizes its main point.
- Use subheadings, bullet points, lists, quotes, or other elements to break up the text and make it easier to read.
- You should explain why the topic is relevant and important for the audience, what problem or challenge it addresses, how it can be solved or improved, what benefits or advantages it offers, and what action or step the reader should take next.
- Use relevant keywords strategically throughout the blog post to optimize it for search engines and attract more readers. You should also avoid keyword stuffing or using irrelevant or misleading keywords that do not match the content of the blog post.
- Use a catchy title, a hook sentence, a clear thesis statement, a compelling story or anecdote, a surprising fact or statistic, a relevant question or challenge, a strong conclusion.
- You should use these components to capture the attention of the reader and convey the main message and purpose of the blog
- The output format of the entire blog post must be in Markdown. All headings, bullet points, links, etc. must use proper Markdown syntax
Please follow these instructions carefully and write a high-quality and original blog post about: {topic}. Start immediately with the content of the blog post:"""
)
