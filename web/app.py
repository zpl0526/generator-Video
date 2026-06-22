# Copyright (C) 2025 AIDC-AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Pixelle-Video Web UI - Main Entry Point

Apple-inspired multi-page navigation:
  Sidebar groups
    🎨 视频创作  (5 pipeline pages)
    📚 视频管理
    ⚙ 系统管理
"""

import sys
from pathlib import Path

# Add project root to sys.path for module imports
_script_dir = Path(__file__).resolve().parent
_project_root = _script_dir.parent
if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

import streamlit as st  # noqa: E402

# Setup page config (must be first Streamlit command)
st.set_page_config(
    page_title="ZPL · Video Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


def get_navigation_group_labels() -> dict[str, str]:
    """Return sidebar navigation group labels with functional icons."""
    return {
        "video_creation": "🎬 视频创作",
        "script_creation": "✍️ 脚本创作",
        "video_management": "📚 视频管理",
        "system_management": "⚙️ 系统管理",
    }


def main():
    """Main entry point with grouped navigation."""
    group_labels = get_navigation_group_labels()
    # Pages — file paths are relative to this app.py location
    quick_create = st.Page(
        "pages/01_quick_create.py",
        title="快速创造",
        default=True,
    )
    digital_human = st.Page(
        "pages/02_digital_human.py",
        title="数字人口播",
    )
    image_to_video = st.Page(
        "pages/03_image_to_video.py",
        title="图生视频",
    )
    action_transfer = st.Page(
        "pages/04_action_transfer.py",
        title="动作迁移",
    )
    asset_based = st.Page(
        "pages/05_asset_based.py",
        title="素材成片",
    )
    history = st.Page(
        "pages/06_history.py",
        title="历史记录",
    )
    settings = st.Page(
        "pages/07_settings.py",
        title="系统配置",
    )
    sensitive_words = st.Page(
        "pages/08_sensitive_words.py",
        title="敏感词配置",
    )
    sensitive_words_detector = st.Page(
        "pages/09_sensitive_words_detector.py",
        title="敏感词检测",
    )
    ai_rewrite = st.Page(
        "pages/10_ai_rewrite.py",
        title="AI仿写",
    )

    pg = st.navigation(
        {
            group_labels["video_creation"]: [
                quick_create,
                digital_human,
                image_to_video,
                action_transfer,
                asset_based,
            ],
            group_labels["script_creation"]: [ai_rewrite, sensitive_words_detector],
            group_labels["video_management"]: [history],
            group_labels["system_management"]: [settings, sensitive_words],
        }
    )
    pg.run()


if __name__ == "__main__":
    main()
