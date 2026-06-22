from web.components.ai_rewrite import build_ai_rewrite_prompt, rewrite_with_ai


def test_build_prompt_contains_original_document_and_required_sections():
    prompt = build_ai_rewrite_prompt("这是一段关于提升专注力的短视频文案。")

    assert "这是一段关于提升专注力的短视频文案。" in prompt
    assert "抖音" in prompt
    assert "小红书" in prompt
    assert "不改变原文章的核心观点" in prompt
    assert "### 标题" in prompt
    assert "### 仿写文案" in prompt
    assert "### 改写说明" in prompt


def test_build_prompt_strips_surrounding_whitespace():
    prompt = build_ai_rewrite_prompt("\n  原始文案  \n")

    assert "<原文>\n原始文案\n</原文>" in prompt


async def test_rewrite_with_ai_uses_expected_prompt_and_parameters():
    captured = {}

    async def fake_llm(**kwargs):
        captured.update(kwargs)
        return "### 标题\n专注力提升指南\n\n### 仿写文案\n改写结果"

    result = await rewrite_with_ai("提升专注力的方法", fake_llm)

    assert "专注力提升指南" in result
    assert "提升专注力的方法" in captured["prompt"]
    assert captured["temperature"] == 0.7
    assert captured["max_tokens"] == 1800
