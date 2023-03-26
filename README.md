## Black Maria

### Getting Started
#### Prerequisites
- [Python 3.6+](https://www.python.org/downloads/)

#### Installation
- export `OPEN_AI_KEY` to your environment variables
- `pip install blackmaria`

### What is Black Maria?
Black Maria is a Python library for web scraping any webpage using natural language.

### How to use Black Maria?
Black Maria uses guardrails https://github.com/ShreyaR/guardrails. Guardrails are a set of instructions that tell the LLM what the output should look like. 

```python
from blackmaria import maria

url="https://yellowjackets.fandom.com/wiki/F_Sharp"
spec=("""
    <rail version="0.1">

    <output>
    </output>

    <prompt>

    Query string here.

    @xml_prefix_prompt

    {output_schema}

    @json_suffix_prompt_v2_wo_none
    </prompt>
    </rail>
    """)
query="provide details about the movie,summary,cast,cast.starring,cast.guest_starring,cast.co-starring"
query_response=maria.night_crawler(url=url,spec=spec,query=query)
print(query_response)

```