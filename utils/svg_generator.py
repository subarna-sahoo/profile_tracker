def generate_svg(view_count: int) -> str:
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
        <rect width="150" height="20" fill="#555"/>
        <text x="10" y="14" fill="#fff" font-family="Verdana" font-size="11">
            👁️ {view_count} views
        </text>
    </svg>
    """
