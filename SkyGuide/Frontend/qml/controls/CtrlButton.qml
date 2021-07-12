import QtQuick 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5


Button
{
    id: ctrlBtn

    property url btnIconSource: "../../images/svg_images/minimize_icon.svg"

    property color btnColorDefault: "#182027"
    property color btnColorMouseOver: "#1f2932"
    property color btnColorClicked: "#00a1f1"

    property int iconWidth: 16
    property int iconHeight: 16

    implicitWidth: 35
    implicitHeight: 35

    background: Rectangle
    {
        id: btnBg
        color: if(ctrlBtn.down)
                   btnColorClicked
                else if(ctrlBtn.hovered)
                   btnColorMouseOver
                else
                   btnColorDefault
        radius: 10

        Image
        {
            id: btnIcon

            anchors.verticalCenter: parent.verticalCenter
            source: btnIconSource
            anchors.horizontalCenter: parent.horizontalCenter

            height: iconHeight
            width:  iconWidth

            fillMode: Image.PreserveAspectFit
        }
        ColorOverlay
        {
            anchors.fill: btnIcon
            source: btnIcon
            color: "#ffffff"
            antialiasing: false
        }
    }
}
