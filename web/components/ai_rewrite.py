# Copyright (C) 2025 AIDC-AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0

"""AI rewrite component for web UI."""

import streamlit as st

from web.i18n import tr
from web.state.session import get_pixelle_video
from web.utils.async_helpers import run_async


def build_ai_rewrite_prompt(document: str) -> str:
    """Build the prompt used to ask the LLM for article rewriting."""
    original_document = document.strip()

    return f"""你是一个擅长抖音和小红书内容创作的文案仿写助手。请在不改变原文章的核心观点、事实信息、立场和主要逻辑的前提下，对原文进行简单改写，降低句式、表达和段落组织与原文的相似度。

改写要求：
1. 不改变原文章的核心观点，不编造新事实，不夸大原文没有表达的效果，开头要有钩子，能吸引人。
2. 保留原文主要信息和内容思想，但替换重复句式、调整表达顺序、口语化表达。
3. 文案要适合抖音或小红书发布，表达自然、有记忆点，但不要标题党。
4. 生成一个符合文案内容的标题，标题应简洁、有吸引力，思想与正文一致，有关键字。
5. 使用 Markdown 输出，并严格包含以下章节：

### 标题
给出 3 个适合发布的标题。

### 仿写文案
给出改写后的完整文案。

### 改写说明
简要说明保留了哪些核心思想，以及主要做了哪些表达调整，按1，2，3点的格式输出

<原文>
{original_document}
</原文>
"""


async def rewrite_with_ai(document: str, llm) -> str:
    """Rewrite document by sending it to the configured LLM."""
    prompt = build_ai_rewrite_prompt(document)
    return await llm(prompt=prompt, temperature=0.7, max_tokens=1800)


def render_ai_rewrite():
    """Render AI rewrite panel."""
    with st.container(border=True):
        st.markdown(f"**{tr('ai_rewrite.card_title')}**")
        st.caption(tr("ai_rewrite.card_caption"))

        document = st.text_area(
            tr("ai_rewrite.input_label"),
            height=360,
            placeholder=tr("ai_rewrite.input_placeholder"),
            help=tr("ai_rewrite.input_help"),
            key="ai_rewrite_document",
        )

        if st.button(
            tr("ai_rewrite.rewrite_btn"),
            type="primary",
            key="ai_rewrite_rewrite_btn",
        ):
            st.session_state.ai_rewrite_result = None
            if not document.strip():
                st.warning(tr("ai_rewrite.empty_input_warning"))
                return

            try:
                core = get_pixelle_video()
                with st.spinner(tr("ai_rewrite.rewriting")):
                    result = run_async(rewrite_with_ai(document, core.llm))
                st.session_state.ai_rewrite_result = result
            except Exception as e:
                st.error(f"{tr('ai_rewrite.rewrite_failed')}: {str(e)}")

        result = st.session_state.get("ai_rewrite_result")
        if result:
            st.divider()
            st.markdown(f"**{tr('ai_rewrite.result_title')}**")
            st.markdown(result)
