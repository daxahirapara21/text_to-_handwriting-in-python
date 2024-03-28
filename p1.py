import pywhatkit as kit
import cv2
writee=input("enter your text:")
kit.text_to_handwriting(writee,save_to="pythoncoding.jpg")
img=cv2.imread("pythoncoding.png")
cv2.imshow("python coding",img)
cv2.waitkey(0)
cv2.destroyAllWindows()
