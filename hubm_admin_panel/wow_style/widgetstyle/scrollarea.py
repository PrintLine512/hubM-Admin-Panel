scrollarea_style = '''
QScrollArea {
    border-style: none;
}

QScrollArea > QWidget > QWidget {
    background-color: palette(alternate-base);
}

QAbstractScrollArea::corner {
    background: transparent;
    border: none;
}
'''
