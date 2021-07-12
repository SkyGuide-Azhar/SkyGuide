import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"


Rectangle
{
    id: homePageRec

    color: "#273139"

    Label
    {
        id: welcomeLabel
        height: 50
        color: "#f1f6ec"
        text: qsTr("Welcome to Sky Guide")
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.weight: Font.Normal
        font.bold: true
        font.italic: false
        font.family: "Times New Roman"
        font.pointSize: 22
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 30
    }
    Image
    {
        id: appLogoImage

        width: 204
        height: 159



        source: "../../images/png_images/galaxy.png"
        anchors.topMargin: 30
        fillMode: Image.PreserveAspectFit

        anchors.top: welcomeLabel.bottom
        anchors.horizontalCenter: parent.horizontalCenter

        antialiasing: false



    }
    ColorOverlay
    {
        source: appLogoImage
        anchors.fill: appLogoImage
        color: "#8491a0"
    }

    Label
    {
        id: msgLabel
        height: 50
        color: "#8491a0"
        text: qsTr("Your tool to navigate and track the sky")
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: appLogoImage.bottom
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.family: "Times New Roman"
        font.italic: true
        anchors.rightMargin: 0
        anchors.topMargin: 10
        font.pointSize: 15
        anchors.leftMargin: 0
        font.bold: false
        font.weight: Font.ExtraLight
    }
    InfoButton
    {
        id: aboutUsBtn
        anchors.top: msgLabel.bottom
        anchors.horizontalCenterOffset: 0
        anchors.topMargin: 50
        anchors.horizontalCenter: parent.horizontalCenter



        onClicked:
        {
            infoBtnAnimation.running = true
            infoRecAnimation.running = true
        }
    }
    PropertyAnimation
    {
        id: infoBtnAnimation

        target: aboutUsBtn
        property: "anchors.horizontalCenterOffset"

        to: if(aboutUsBtn.anchors.horizontalCenterOffset == 0)
                -300
            else
                0

        duration: 1000
        easing.type: Easing.InOutQuint
    }
    PropertyAnimation
    {
        id: infoRecAnimation

        target: infoRec
        property: "width"

        to: if(infoRec.width == 0)
                500
            else
                0
        duration: 1000
        easing.type: Easing.InOutQuint
    }

    Rectangle
    {
        id: infoRec
        width: 0


        color: homePageRec.color

        radius: 10

        anchors.left: aboutUsBtn.right
        anchors.top: msgLabel.bottom
        anchors.bottom: parent.bottom
        anchors.leftMargin: 50
        anchors.bottomMargin: 15
        anchors.topMargin: 50

        ScrollView
        {
            id: scrollView
            anchors.fill: parent
            anchors.rightMargin: 5
            anchors.leftMargin: 5
            anchors.bottomMargin: 5
            anchors.topMargin: 5
            clip: true

            Text
            {
                color: "#ffffff"
                anchors.fill: parent

                font.family: "Verdana"
                font.weight: Font.ExtraLight
                font.pointSize: 10
                text: qsTr("This application was developed by SkyGuide team:-

        Eng. Sherif Gamal Abdelatef
        Eng. Abdelrahman Farouk Saied
        Eng. Attia Ali Saied Attia
        Eng. Ahmed Sedek Ali
        Eng. Ahmed Ragab

Students at El-Azhar University,
Faculty of Engineering, Dep. Systems and Computers;
This application is part of our graduation project.
")


            }
        }
    }


}



/*##^##
Designer {
    D{i:0;autoSize:true;height:800;width:900}
}
##^##*/
