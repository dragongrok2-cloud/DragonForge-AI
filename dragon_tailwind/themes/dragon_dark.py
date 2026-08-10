"""Dragon-Tailwind theme: тёмная драконья палитра."""

DRAGON_THEME = {
    # Основные цвета
    "primary": "#9F1239",          # Глубокий драконий красный (кровь + рубин)
    "primary_hover": "#BE123C",
    "accent": "#F59E0B",           # Огненный оранжевый / золото
    "accent_soft": "#FBBF24",
    "background": "#0F172A",       # Тёмная ночь
    "surface": "#1E293B",          # Чешуя / поверхность
    "surface_elevated": "#334155",
    "text": "#F1F5F9",             # Светлый текст
    "text_muted": "#94A3B8",
    "scales": "#64748B",           # Чешуя
    "border": "#475569",
    "success": "#10B981",          # Зелёный огонёк
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "info": "#38BDF8",

    # Семантические токены для UI
    "saddle": "#92400E",           # Коричневый седла
    "wing": "#7C3AED",             # Фиолетовый крыла
    "fire": "#F97316",
    "ember": "#FB923C",
}

# CSS-переменные для удобного использования
CSS_VARIABLES = """
:root {
  --dragon-primary: #9F1239;
  --dragon-primary-hover: #BE123C;
  --dragon-accent: #F59E0B;
  --dragon-accent-soft: #FBBF24;
  --dragon-bg: #0F172A;
  --dragon-surface: #1E293B;
  --dragon-surface-elevated: #334155;
  --dragon-text: #F1F5F9;
  --dragon-text-muted: #94A3B8;
  --dragon-scales: #64748B;
  --dragon-border: #475569;
  --dragon-saddle: #92400E;
  --dragon-wing: #7C3AED;
  --dragon-fire: #F97316;
  --dragon-ember: #FB923C;
}
""".strip()

def get_theme_css() -> str:
    """Вернуть готовый блок CSS с переменными темы."""
    return CSS_VARIABLES
