import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5

Button
{
    id: clearBtn

    property color btnDefaultColor: "#00000000"
    property color btnMouseOverColor: "#3c4c58"
    property color btnPressedColor: "#3c4c58"

    background: Rectangle
    {
        color: if(clearBtn.down)
                   btnPressedColor
               else if(clearBtn.hovered)
                   btnMouseOverColor
               else
                   btnDefaultColor

        anchors.fill: parent
        border.color :"#ffffff"
        radius:5

        Text
        {
            color: "#64aafa"

            text: qsTr("Clear")
            font.family: "Arial"
            font.pointSize: 13
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

        }
    }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
