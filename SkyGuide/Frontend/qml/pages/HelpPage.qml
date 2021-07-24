import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "../controls"

Rectangle
{
    id: pageBgRec
    color: "#00000000"

    Label
    {
        id: tmpLabel
        text: "Help Page"
        color: "#ababab"
        anchors.verticalCenter: parent.verticalCenter
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        font.bold: true
        font.family: "Times New Roman"
        font.pointSize: 40
        anchors.horizontalCenter: parent.horizontalCenter


    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
