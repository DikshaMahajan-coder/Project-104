import cv2

img = cv2.imread("solar-system.jpg.")

cv2.putText(img,
            "Sun",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (110,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Venus",
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Earth",
            (290,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Moon",
            (320,155),
            cv2.FONT_HERSHEY_COMPLEX,
            0.3,
            (225,225,225)
            )

cv2.putText(img,
            "Mars",
            (380,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Jupiter",
            (560,380),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Saturn",
            (770,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Uranus",
            (970,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )

cv2.putText(img,
            "Neptune",
            (1100,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (225,225,225)
            )


cv2.imshow("solar-system.jpg",img)
cv2.waitKey(0)
