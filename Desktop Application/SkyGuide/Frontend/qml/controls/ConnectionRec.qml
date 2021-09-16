import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5


Rectangle
{
    id: connectionRec
    color: "#273139"

    property bool connectionState: false

    Image
    {
        id: connectionImage
        width: 50
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        source: "../../images/svg_images/wi-fi.svg"
        anchors.leftMargin: 35
        anchors.bottomMargin: 2
        anchors.topMargin: 2
        fillMode: Image.PreserveAspectFit

        ColorOverlay
        {
            color: if(connectionState)
                       "#00aa00"
                   else
                       "#ff0000"
            anchors.fill: parent
            source: connectionImage
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            antialiasing: false

        }
    }

    Label
    {
        id: connectionLabel
        color: "#c7c7c7"
        text: if(connectionState)
                  "Connected"
              else
                  "Not Connected"
        anchors.left: connectionImage.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        font.weight: Font.ExtraLight
        font.family: "Arial"
        font.pointSize: 13
        anchors.leftMargin: 0
        anchors.rightMargin: 0
        anchors.topMargin: 0
        anchors.bottomMargin: 0
    }


}

/*##^##
Designer {
    D{i:0;autoSize:true;formeditorZoom:3;height:20;width:200}D{i:3;locked:true}
}
##^##*/
