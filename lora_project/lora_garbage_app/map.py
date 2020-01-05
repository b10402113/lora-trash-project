import matplotlib.pyplot as plt   # 匯入繪圖模組
import numpy as np               #  匯入需要生成資料的numpy模組
import cv2
from django.contrib.staticfiles.storage import staticfiles_storage

class draw_path:
    def __init__(self):
        # img_url = staticfiles_storage.path('img/imgage.jpg')
        url = 'static/img/image.jpg'
        self.img = cv2.imread(url)
        self.point_size = 10
        self.point_color = (0, 0, 255)
        self.thickness = 4

    def map(self,first_node,second_node):
        cv2.line(self.img, first_node, second_node, (0, 0, 255), self.thickness)
        # #路徑 A->B
        #     if first_node == (560,440) and second_node == (605,700):
        #         cv2.line(self.img,(560,440),(580,440),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,440),(580,700),(0,100,255),self.thickness)
        #         cv2.line(self.img,(580,700),(605,700),(80, 113, 0),self.thickness)
        # #路徑 A->C
        #     elif first_node == (560,440) and second_node == (860,535):
        #         cv2.line(self.img,(560,440),(580,440),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,440),(580,510),(0,100,255),self.thickness)
        #         cv2.line(self.img,(580,510),(860,510),(80,113,0),self.thickness)
        #         cv2.line(self.img,(860,510),(860,535),(80,113,145),self.thickness)
        # #路徑 A->D
        #     elif first_node == (560,440) and second_node == (1020,535):
        #         cv2.line(self.img,(560,440),(580,440),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,440),(580,510),(0,255,0),self.thickness)
        #         cv2.line(self.img,(580,510),(1020,510),(255,0,0),self.thickness)
        #         cv2.line(self.img,(1020,510),(1020,535),(127,127,127),self.thickness)
        # #路徑 A->E
        #     elif first_node == (560,440) and second_node == (890,270):
        #         cv2.line(self.img,(560,440),(610,440),(0,0,255),self.thickness)
        #         cv2.line(self.img,(610,440),(610,295),(0,0,255),self.thickness)
        #         cv2.line(self.img,(610,295),(890,295),(0,0,255),self.thickness)
        #         cv2.line(self.img,(890,295),(890,270),(0,0,255),self.thickness)
        # #路徑 A->F
        #     elif first_node == (560,440) and second_node == (1250,375):
        #         cv2.line(self.img,(560,440),(580,440),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,440),(580,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,510),(1250,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1250,510),(1250,375),(0,0,255),self.thickness)
        # #路徑 B->C
        #     elif first_node == (605,700) and second_node == (860,535):
        #         cv2.line(self.img,(605,700),(580,700),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,700),(580,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,510),(860,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(860,510),(860,535),(0,0,255),self.thickness)
        # #路徑 B->D
        #     elif first_node == (605,700) and second_node == (1020,535):
        #         cv2.line(self.img,(605,700),(580,700),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,700),(580,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,510),(1020,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1020,510),(1020,535),(0,0,255),self.thickness)
        # #路徑 B->E
        #     elif first_node == (605,700) and second_node == (890,270):
        #         cv2.line(self.img,(605,700),(580,700),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,700),(580,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,510),(890,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(890,510),(890,270),(0,0,255),self.thickness)
        # #路徑 B->F
        #     elif first_node == (605,700) and second_node == (890,270):
        #         cv2.line(self.img,(605,700),(580,700),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,700),(580,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(580,510),(1250,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1250,510),(1250,375),(0,0,255),self.thickness)
        # #路徑 C->D
        #     elif first_node == (860,535) and second_node == (1020,535):
        #         cv2.line(self.img,(860,535),(860,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(860,510),(1020,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1020,510),(1020,535),(0,0,255),self.thickness)
        #
        # #路徑 C->E
        #     elif first_node == (860,535) and second_node == (890,270):
        #         cv2.line(self.img,(860,535),(860,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(860,510),(890,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(890,510),(890,270),(0,0,255),self.thickness)
        # #路徑 C->F
        #     elif first_node == (860,535) and second_node == (1250,375):
        #         cv2.line(self.img,(860,535),(860,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(860,510),(1250,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1250,510),(1250,375),(0,0,255),self.thickness)
        # #路徑 D->E
        #     elif first_node == (1020,535) and second_node == (1250,375):
        #         cv2.line(self.img,(1020,535),(1020,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1020,510),(1250,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1250,510),(1250,375),(0,0,255),self.thickness)
        # #路徑 D->F
        #     elif first_node == (1020,535) and second_node == (890,270):
        #         cv2.line(self.img,(1020,535),(1020,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1020,510),(890,510),(0,0,255),self.thickness)
        #         cv2.line(self.img,(890,510),(890,270),(0,0,255),self.thickness)
        # #路徑 E->F
        #     elif first_node == (890,270) and second_node == (1250,375):
        #         cv2.line(self.img,(890,270),(1250,270),(0,0,255),self.thickness)
        #         cv2.line(self.img,(1250,270),(1250,375),(0,0,255),self.thickness)
        #     else:
        #         print("錯誤路徑")


    def start_draw(self,paths):
        print("=== 繪圖開始 ===")
        for path in paths:
            location_1 = path[0]
            location_2 = path[1]
            self.map(location_1,location_2)

    def put_text(self):
        # cv2.putText(self.img,"A=("+str(560)+","+str(440)+")",(560+25,440+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.putText(self.img,"B=("+str(605)+","+str(700)+")",(605+20,700+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.putText(self.img,"C=("+str(860)+","+str(535)+")",(860+20,535+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.putText(self.img,"D=("+str(1020)+","+str(535)+")",(1020+20,535+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.putText(self.img,"E=("+str(890)+","+str(270)+")",(890+20,270+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.putText(self.img,"F=("+str(1250)+","+str(375)+")",(1250+20,375+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.putText(self.img, "(x_range,y_range) = (1680,987)", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
        point_list = [(560, 440), (605, 700), (860, 535), (1020, 535), (890, 270), (1250, 375)]
        for point in point_list:
            cv2.circle(self.img, point, self.point_size, self.point_color, self.thickness)
            # cv2.putText(self.img,"("+str(point[0])+","+str(point[1])+")",(point[0]+20,point[1]+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
        # cv2.imshow('My Image', self.img)

        cv2.imwrite('static/img/new_image.jpg', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("繪圖結束")






