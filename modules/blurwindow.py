#source: https://github.com/Opticos/GWSL-Source/blob/master/blur.py , https://www.cnblogs.com/zhiyiYo/p/14659981.html , https://github.com/ifwe/digsby/blob/master/digsby/src/gui/vista.py
import platform
import ctypes

# Main code taken from https://pypi.org/project/BlurWindow/

if platform.system() == 'Windows':
    from ctypes.wintypes import  DWORD, BOOL, HRGN, HWND
    user32 = ctypes.windll.user32
    dwm = ctypes.windll.dwmapi


    class ACCENTPOLICY(ctypes.Structure):
        _fields_ = [
            ("AccentState", ctypes.c_uint),
            ("AccentFlags", ctypes.c_uint),
            ("GradientColor", ctypes.c_uint),
            ("AnimationId", ctypes.c_uint)
        ]


    class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
        _fields_ = [
            ("Attribute", ctypes.c_int),
            ("Data", ctypes.POINTER(ctypes.c_int)),
            ("SizeOfData", ctypes.c_size_t)
        ]


    class DWM_BLURBEHIND(ctypes.Structure):
        _fields_ = [
            ('dwFlags', DWORD), 
            ('fEnable', BOOL),  
            ('hRgnBlur', HRGN), 
            ('fTransitionOnMaximized', BOOL) 
        ]


    class MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)
                    ]


    SetWindowCompositionAttribute = user32.SetWindowCompositionAttribute

def ExtendFrameIntoClientArea(hwnd):

    class _MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)
                    ]

    DwmExtendFrameIntoClientArea = dwm.DwmExtendFrameIntoClientArea
    m = _MARGINS()
    m.cxLeftWidth = 0
    m.cxRightWidth = 0
    m.cyTopHeight = 0
    m.cyBottomHeight = 25
    return DwmExtendFrameIntoClientArea(hwnd, m)

def HEXtoRGBAint(HEX:str):
    alpha = HEX[7:]
    blue = HEX[5:7]
    green = HEX[3:5]
    red = HEX[1:3]

    gradientColor = alpha + blue + green + red
    return int(gradientColor, base=16)


def ApplyBlur(hwnd, hexColor=False, Acrylic=False, Dark=False, smallCorners=False):
    accent = ACCENTPOLICY()
    accent.AccentState = 3 #Default window Blur #ACCENT_ENABLE_BLURBEHIND

    gradientColor = 0
    
    if hexColor != False:
        gradientColor = HEXtoRGBAint(hexColor)
        accent.AccentFlags = 2 #Window Blur With Accent Color #ACCENT_ENABLE_TRANSPARENTGRADIENT
    
    if Acrylic:
        accent.AccentState = 4 #UWP but LAG #ACCENT_ENABLE_ACRYLICBLURBEHIND
        if hexColor == False: #UWP without color is translucent
            accent.AccentFlags = 2
            gradientColor = HEXtoRGBAint('#12121240') #placeholder color
    
    accent.GradientColor = gradientColor
    
    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19 #WCA_ACCENT_POLICY
    data.SizeOfData = ctypes.sizeof(accent)
    data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.POINTER(ctypes.c_int))
    
    SetWindowCompositionAttribute(int(hwnd), data)
    
    if Dark: 
        data.Attribute = 26 #WCA_USEDARKMODECOLORS
    
        SetWindowCompositionAttribute(int(hwnd), data)
    

    DwmSetWindowAttribute = dwm.DwmSetWindowAttribute #  Add rounded borders (My addition)
    DwmSetWindowAttribute(int(hwnd), 33, ctypes.byref(ctypes.c_int(2 if smallCorners else 0)), ctypes.sizeof(ctypes.c_int)) # Add rounded borders (My addition)



def GlobalBlur(HWND,hexColor=False,Acrylic=False,Dark=False,QWidget=None, smallCorners=False):
    ApplyBlur(HWND,hexColor,Acrylic,Dark, smallCorners=smallCorners)
