# Copyright (C) 2025 AIDC-AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0

"""AI rewrite page — rewrites scripts while preserving original meaning."""

from web.components.ai_rewrite import render_ai_rewrite
from web.components.theme import render_section_title
from web.i18n import tr
from web.utils.page_bootstrap import bootstrap

bootstrap()

render_section_title(
    title=tr("ai_rewrite.title", fallback="AI仿写"),
    subtitle=tr(
        "ai_rewrite.subtitle",
        fallback="输入原文后，AI 将在保留核心思想的前提下改写文案，并生成适合发布的标题。",
    ),
)

render_ai_rewrite()
