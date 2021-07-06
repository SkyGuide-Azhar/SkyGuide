import QtQuick 2.0
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5



Button
{
    id: menuBtn

    property string btnText: qsTr("Home")

    property color btnDefaultColor     : "#00000000"
    property color btnMouseOverColor   : "#1f2932"
    property color btnMousePressedColor: "#273139"

    property int iconWidth: 20
    property int iconHeight: 20
    property url btnImageSource: "../../images/svg_images/home_icon.svg"
    clip: true

    implicitWidth: 160
    implicitHeight: 60

    Rectangle
    {
        id: btnTopRec
        color: "#ff8f70"
        height: 2

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right

        anchors.topMargin: 0
        anchors.leftMargin: 0
        anchors.rightMargin: 0

        visible: if(btnDefaultColor == btnMousePressedColor)
                     true
                else
                     false
    }

    Text
    {
        id: btnTxt
        width: 90
        color: "#ffffff"
        text: menuBtn.btnText


        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        anchors.bottomMargin: 17
        anchors.topMargin: 17
        anchors.leftMargin: 40

        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter

        clip: true
        font.pointSize: 10
    }

    background: Rectangle
    {
        id: btnBgRec

        anchors.fill: parent

        color: if(menuBtn.down)
                   btnMousePressedColor
               else if (menuBtn.hovered)
                   btnMouseOverColor
               else
                   btnDefaultColor

        Image
        {
            id: btnImage
            source: btnImageSource
            fillMode: Image.PreserveAspectFit

            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.leftMargin: 10


            sourceSize.width:  iconWidth
            sourceSize.height: iconHeight
            height: iconHeight
            width:  iconWidth

            antialiasing: true
        }
        ColorOverlay
        {
            anchors.fill: btnImage
            source: btnImage
            color: "#ffffff"
            antialiasing: true
        }

    }

}


/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:1.25;height:60;width:160}
}
##^##*/
