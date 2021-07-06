import QtQuick 2.0
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
Button
{
    id: aboutUsBtn

    width: 145
    height: 50

    property color btnDefaultColor: "#64aafa"
    property color btnMouseOverColor: "#a3ceff"
    property color btnPressedColor: "#aaffff"
    property string btnTxt: "About Us"

    property url btnImage: "../../images/svg_images/info.svg"
    property int btnImageWidth: 25
    property int btnImageHeight: 15

    font.pointSize: 15

    background: Rectangle
    {
        id: btnBgRec
        radius: 10
        anchors.fill: parent
        color: if(aboutUsBtn.down)
                   btnPressedColor
               else if(aboutUsBtn.hovered)
                   btnMouseOverColor
               else
                   btnDefaultColor

        Image
        {
            id: infoImage
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            source: btnImage
            sourceSize.height: btnImageHeight
            sourceSize.width: btnImageWidth
            fillMode: Image.PreserveAspectFit
            anchors.leftMargin: 10

            ColorOverlay
            {
                color: "#182027"
                source: infoImage
                anchors.fill: infoImage
                antialiasing: false

            }

        }
        Text
        {
            id: btnText
            color: "#1f2027"
            text: btnTxt
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            font.pointSize: aboutUsBtn.font.pointSize
            anchors.leftMargin: 40
        }
    }
}


