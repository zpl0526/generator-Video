import inspect

from web import app
from web.components import theme


def test_navigation_group_labels_include_icons():
    labels = app.get_navigation_group_labels()

    assert labels == {
        "video_creation": "🎬 视频创作",
        "script_creation": "✍️ 脚本创作",
        "video_management": "📚 视频管理",
        "system_management": "⚙️ 系统管理",
    }


def test_secondary_navigation_items_do_not_define_icons():
    source = inspect.getsource(app.main)

    assert "icon=" not in source


def test_sidebar_theme_uses_compact_width():
    css = theme._THEME_CSS

    assert "width: 200px" in css
    assert "min-width: 200px" in css
    assert "max-width: 200px" in css


def test_sidebar_theme_supports_independent_scroll():
    css = theme._THEME_CSS

    assert 'section[data-testid="stSidebar"] > div:first-child' in css
    assert "height: 100vh" in css
    assert "overflow-y: auto" in css
    assert "overscroll-behavior: contain" in css


def test_sidebar_theme_removes_navigation_indentation():
    css = theme._THEME_CSS

    assert '[data-testid="stSidebarNav"] ul' in css
    assert "padding-left: 0" in css
    assert "margin-left: 0" in css
    assert "--pv-sidebar-x" in css


def test_sidebar_secondary_items_use_compact_spacing():
    css = theme._THEME_CSS

    assert "min-height: 32px" in css
    assert "padding: 6px var(--pv-sidebar-x)" in css
    assert "margin: 1px 0" in css


def test_sidebar_section_titles_have_hover_and_expanded_state():
    css = theme._THEME_CSS
    script = theme._SIDEBAR_NAV_JS

    assert 'section > div > span:hover' in css
    assert "background: var(--pv-brand-soft)" in css
    assert "color: var(--pv-brand)" in css
    assert "rgba(79, 70, 229, 0.14)" in css
    assert "pv-sidebar-nav-expanded" in css
    assert "pv-sidebar-nav-expanded" in script


def test_sidebar_section_titles_show_right_aligned_chevron():
    css = theme._THEME_CSS
    script = theme._SIDEBAR_NAV_JS

    assert "pv-sidebar-chevron" in css
    assert "right: var(--pv-sidebar-x)" in css
    assert "border-right: 2px solid #4b5563" in css
    assert "border-bottom: 2px solid #4b5563" in css
    assert "rotate(45deg)" in css
    assert "rotate(-135deg)" in css
    assert "ensureChevron" in script
    assert "pv-sidebar-section-title" in css
    assert "title.classList.add('pv-sidebar-section-title')" in script
    assert "ROOT_DOC.createElement('span')" in script
    assert "title.appendChild(chevron)" in script


def test_sidebar_nav_script_is_injected_with_components_html():
    source = inspect.getsource(theme._inject_sidebar_nav_behavior)

    assert "streamlit.components.v1" in source
    assert "_components_html(_SIDEBAR_NAV_JS" in source


def test_sidebar_theme_has_collapsible_navigation_script():
    script = theme._SIDEBAR_NAV_JS

    assert "pv-sidebar-nav-collapsed" in script
    assert "pv-sidebar-nav-ready" in script
    assert "stSidebarNavLink" in script
    assert "MutationObserver" in script


def test_sidebar_nav_script_resets_collapsed_state_on_reload():
    script = theme._SIDEBAR_NAV_JS

    assert "resetSectionCollapsedState" in script
    assert "enhanceSidebarNav(true)" in script
    assert "enhanceSidebarNav(false)" in script
    assert "resetSectionCollapsedState(section, title)" in script
    assert script.index("resetSectionCollapsedState(section, title)") < script.index(
        "section.dataset[NAV_READY] === '1'"
    )
