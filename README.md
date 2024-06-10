# PyQt6

Martin Fitzpatrick - Create GUI Applications with Python &amp; Qt6 (PyQt6 Edition)

Notes from the textbook

1. As well as .setFixedSize() you can also call .setMinimumSize() and .setMaximumSize() to set the minimum and maximum sizes respectively.

**_Widgets_**

```python
# Widget                 | What it does
# _______________________|______________________________
# QCheckbox              | A checkbox
# QComboBox              | A dropdown list box
# QDateEdit              | For editing dates
# QDateTimeEdit          | For editing dates and datetimes
# QDial                  | Rotatable dial
# QDoubleSpinbox         | A number spinner for floats
# QFontComboBox          | A list of fonts
# QLCDNumber             | A quite ugly LCD display
# QLabel                 | Just a label, not interactive
# QLineEdit              | Enter a line of text
# QProgressBar           | A progress bar
# QPushButton            | A button
# QRadioButton           | A group with only one active choice
# QSlider                | A slider
# QSpinBox               | An integer spinner
# QTimeEdit              | For editing time

```

```python
# The flags available for horizontal alignment are —

# Flag                                       | Behavior
# ______________________________________________________________________________________________
# Qt.AlignmentFlag.AlignLeft                 | Aligns with the left edge.
# Qt.AlignmentFlag.AlignRight                | Aligns with the right edge.
# Qt.AlignmentFlag.AlignHCenter              | Centers horizontally in the available space.
# Qt.AlignmentFlag.AlignJustify              | Justifies the text in the available space.

# The flags available for vertical alignment are —

# Flag                                       | Behavior
# ____________________________________________________________________________________________
# Qt.AlignmentFlag.AlignTop                  | Aligns with the top.
# Qt.AlignmentFlag.AlignBottom               | Aligns with the bottom.
# Qt.AlignmentFlag.AlignVCenter              | Centers vertically in the available space
```
