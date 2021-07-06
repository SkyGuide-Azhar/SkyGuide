import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.5
import "controls"

Window
{
    id: mainWindow
    x: 250
    y: 50
    visible: true
    title: qsTr("Sky Guide")
    color: "#00000000"

    flags: Qt.Window | Qt.FramelessWindowHint

    width: 820
    minimumWidth: 820

    height: 700
    minimumHeight: 700

    property int bgMargin: 5
    property string currectPage: "home"

    property bool internetConnected: false
    property bool isFirstLoad: true


    Rectangle
    {
        id: bgRec
        color: "#273139"

        radius: 10

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        anchors.rightMargin: bgMargin
        anchors.leftMargin: bgMargin
        anchors.bottomMargin: bgMargin
        anchors.topMargin: bgMargin

        Rectangle
        {
            id: topAreaRec
            height: 110
            color: "#182027"

            radius:if(maximizeBtn.isWindowMaximized)
                       0
                   else
                       10

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top

            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0

            Rectangle
            {
                id: appTitleRec
                color: "#00000000"

                radius: 10

                anchors.left: parent.left
                anchors.right: ctrlButtonsRec.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 5

                anchors.bottomMargin: 65
                anchors.leftMargin: 0
                anchors.topMargin: 0

                DragHandler
                {
                    onActiveChanged: if(active && !maximizeBtn.isWindowMaximized)
                                         mainWindow.startSystemMove()
                }

                Image
                {
                    id: appIcon
                    width: 50

                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 5

                    horizontalAlignment: Image.AlignHCenter
                    verticalAlignment: Image.AlignBottom

                    source: "../images/svg_images/galaxy.svg"
                    fillMode: Image.PreserveAspectFit

                }
                ColorOverlay
                {
                    anchors.fill: appIcon
                    source: appIcon
                    color: "#bebebe"

                }

                Label
                {
                    id: appTiltleLabel
                    color: "#ffffff"
                    text: qsTr("Sky Guide")

                    anchors.left: appIcon.right
                    anchors.right: parent.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.rightMargin: 0
                    anchors.leftMargin: 5
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    verticalAlignment: Text.AlignVCenter
                    font.styleName: "Regular"
                    font.weight: Font.ExtraLight
                    font.family: "Times New Roman"
                    font.italic: false
                    font.pointSize: 19
                }
            }

            Rectangle
            {
                id: ctrlButtonsRec
                width: 110
                color: "#00000000"

                radius: 10

                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom

                anchors.bottomMargin: 60
                anchors.rightMargin: 0
                anchors.topMargin: 0

                CtrlButton
                {
                    id: minmizeBtn

                    anchors.right: maximizeBtn.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 15
                    anchors.topMargin: 0
                    anchors.rightMargin: 0

                    onClicked: mainWindow.showMinimized()
                }
                CtrlButton
                {
                    id: maximizeBtn
                    anchors.right: closeBtn.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 15
                    anchors.topMargin: 0
                    anchors.rightMargin: 0
                    btnIconSource: if(isWindowMaximized)
                                       "../images/svg_images/restore_icon.svg"
                                   else
                                       "../images/svg_images/maximize_icon.svg"

                    property bool isWindowMaximized: false

                    onClicked: if(isWindowMaximized)
                               {
                                   isWindowMaximized = false
                                   bgMargin = 5
                                   mainWindow.showNormal()
                               }
                                else
                               {
                                   isWindowMaximized = true
                                   bgMargin = 0
                                   mainWindow.showMaximized()
                               }
                }
                CtrlButton
                {
                    id: closeBtn
                    anchors.right: parent.right
                    anchors.rightMargin: 0

                    btnColorClicked: "#aa0000"
                    btnColorMouseOver: "#aa0000"

                    iconWidth: 13
                    iconHeight: 13
                    btnIconSource: "../images/svg_images/on-off-button.svg"

                    onClicked: mainWindow.close()

                }
            }

            Rectangle
            {
                id: menuRec
                color: "#00000000"

                radius: 10

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: appTitleRec.bottom
                anchors.bottom: parent.bottom

                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.leftMargin: 0
                anchors.topMargin: 15

                MenuButton
                {
                    id: homeBtn
                    width: 85

                    anchors.left: parent.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.leftMargin: 0
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0
                    btnText: "Home"

                    btnDefaultColor: bgRec.color

                    onClicked:
                    {
                        homeSearchSep.visible = false
                        searchExploreSep.visible = true
                        exploreAddSep.visible = true
                        addHelpSep.visible = true

                        homeBtn.btnDefaultColor = bgRec.color
                        searchInDBbtn.btnDefaultColor = topAreaRec.color
                        exploreBtn.btnDefaultColor = topAreaRec.color
                        addToDBbtn.btnDefaultColor = topAreaRec.color
                        helpBtn.btnDefaultColor = topAreaRec.color

                        if(currectPage != "home")
                        {
                            pagesStackView.push(Qt.resolvedUrl("pages/HomePage.qml"))
                            currectPage = "home"
                        }
                    }

                }
                Rectangle
                {
                    id: homeSearchSep
                    color: "#273139"

                    anchors.left: homeBtn.right
                    anchors.right: searchInDBbtn.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 15
                    anchors.topMargin: 15
                    visible: false
                }
                MenuButton
                {
                    id: searchInDBbtn
                    width: 90

                    anchors.left: homeBtn.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.leftMargin: 2
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    btnImageSource: "../images/svg_images/searching-in-database.svg"
                    btnText: "Search"

                    onClicked:
                    {
                        if(internetConnected)
                        {
                            homeSearchSep.visible = false
                            searchExploreSep.visible = false
                            exploreAddSep.visible = true
                            addHelpSep.visible = true

                            homeBtn.btnDefaultColor = topAreaRec.color
                            searchInDBbtn.btnDefaultColor = bgRec.color
                            exploreBtn.btnDefaultColor = topAreaRec.color
                            addToDBbtn.btnDefaultColor = topAreaRec.color
                            helpBtn.btnDefaultColor = topAreaRec.color

                            if(currectPage != "search")
                            {
                                pagesStackView.push(Qt.resolvedUrl("pages/SearchPage.qml"))
                                currectPage = "search"
                            }
                        }
                    }

                }
                Rectangle
                {
                    id: searchExploreSep
                    color: "#273139"

                    anchors.left: searchInDBbtn.right
                    anchors.right: exploreBtn.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 15
                    anchors.topMargin: 15
                }
                MenuButton
                {
                    id: exploreBtn
                    width: 93

                    anchors.left: searchInDBbtn.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.leftMargin: 2
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    btnImageSource: "../images/svg_images/explore.svg"
                    btnText: "Explore"

                    onClicked:
                    {
                        if(!isFirstLoad)
                        {
                            homeSearchSep.visible = true
                            searchExploreSep.visible = false
                            exploreAddSep.visible = false

                            homeBtn.btnDefaultColor = topAreaRec.color
                            searchInDBbtn.btnDefaultColor = topAreaRec.color
                            exploreBtn.btnDefaultColor = bgRec.color
                            addToDBbtn.btnDefaultColor = topAreaRec.color
                            helpBtn.btnDefaultColor = topAreaRec.color

                            if(currectPage != "explore")
                            {
                                pagesStackView.push(Qt.resolvedUrl("pages/ExplorePage.qml"))
                                currectPage = "explore"
                            }
                        }
                    }

                }
                Rectangle
                {
                    id: exploreAddSep
                    color: "#273139"

                    anchors.left: exploreBtn.right
                    anchors.right: addToDBbtn.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 15
                    anchors.topMargin: 15
                }
                MenuButton
                {
                    id: addToDBbtn
                    width: 75

                    anchors.left: exploreBtn.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    iconHeight: 20
                    iconWidth: 18

                    anchors.leftMargin: 2
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    btnImageSource: "../images/svg_images/add-database.svg"
                    btnText: "Add"

                    onClicked:
                    {
                        if(internetConnected)
                        {
                            homeSearchSep.visible = true
                            searchExploreSep.visible = true
                            exploreAddSep.visible = false
                            addHelpSep.visible = false

                            homeBtn.btnDefaultColor = topAreaRec.color
                            searchInDBbtn.btnDefaultColor = topAreaRec.color
                            exploreBtn.btnDefaultColor = topAreaRec.color
                            addToDBbtn.btnDefaultColor = bgRec.color
                            helpBtn.btnDefaultColor = topAreaRec.color

                            if(currectPage != "Add")
                            {
                                pagesStackView.push(Qt.resolvedUrl("pages/AddPage.qml"))
                                currectPage = "Add"
                            }
                        }
                    }

                }
                Rectangle
                {
                    id: addHelpSep
                    color: "#273139"

                    anchors.left: addToDBbtn.right
                    anchors.right: helpBtn.left
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.rightMargin: 0
                    anchors.leftMargin: 0
                    anchors.bottomMargin: 15
                    anchors.topMargin: 15
                }
                MenuButton
                {
                    id: helpBtn
                    width: 80

                    anchors.left: addToDBbtn.right
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom

                    anchors.leftMargin: 2
                    anchors.bottomMargin: 0
                    anchors.topMargin: 0

                    btnImageSource: "../images/svg_images/help.svg"
                    btnText: "Help"

                    onClicked:
                    {
                        homeSearchSep.visible = true
                        searchExploreSep.visible = true
                        exploreAddSep.visible = true
                        addHelpSep.visible = false

                        homeBtn.btnDefaultColor = topAreaRec.color
                        searchInDBbtn.btnDefaultColor = topAreaRec.color
                        exploreBtn.btnDefaultColor = topAreaRec.color
                        addToDBbtn.btnDefaultColor = topAreaRec.color
                        helpBtn.btnDefaultColor = bgRec.color

                        if(currectPage != "help")
                        {
                            pagesStackView.push(Qt.resolvedUrl("pages/HelpPage.qml"))
                            currectPage = "help"
                        }
                    }

                }




            }


        }

        Rectangle
        {
            id: bottomRec
            radius: 10

            width: 200
            height: 20

            color: "#273139"


            anchors.left: parent.left
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0

            Image
            {
                id: resizeCornnerImage

                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0

                visible: !maximizeBtn.isWindowMaximized

                horizontalAlignment: Image.AlignRight
                verticalAlignment: Image.AlignBottom

                source: "../images/svg_images/resize_icon.svg"

                fillMode: Image.PreserveAspectFit
                antialiasing: false

                /* Cornner Resize */
                MouseArea
                {
                    id: resizeCornner
                    anchors.fill: parent

                    cursorShape: Qt.SizeFDiagCursor
                    DragHandler
                    {
                        onActiveChanged: if(active && !maximizeBtn.isWindowMaximized)
                                             mainWindow.startSystemResize(Qt.RightEdge | Qt.BottomEdge)
                    }
                }
            }

            Label {
                id: label
                width: 150
                color: "#ffffff"
                text: qsTr("@SkyGuide-Azhar")
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                verticalAlignment: Text.AlignVCenter
                font.italic: true
                font.pointSize: 10
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0
            }

            Rectangle
            {
                id: connectionRec
                x: 542
                width: 200
                color: "#00000000"

                visible: true

                anchors.right: resizeCornnerImage.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0

                ConnectionRec
                {
                    anchors.fill: parent

                    connectionState: internetConnected

                }

            }
        }

        Rectangle
        {
            id: pageRec
            height: 200
            color: "#00000000"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: topAreaRec.bottom
            anchors.bottom: bottomRec.top
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0

            StackView {
                id: pagesStackView
                anchors.fill: parent
                clip: true             
                initialItem: Qt.resolvedUrl("pages/HomePage.qml")
            }
        }

    }

    // MouseArea(s) for resizing ,,

        /* Left Resize */
        MouseArea
        {
            id: resizeLeft
            width: 5
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.leftMargin: 0
            anchors.bottomMargin: 10
            anchors.topMargin: 10

            visible: !maximizeBtn.isWindowMaximized

            cursorShape: Qt.SizeHorCursor
            DragHandler
            {
                onActiveChanged: if(active && !maximizeBtn.isWindowMaximized)
                                     mainWindow.startSystemResize(Qt.LeftEdge)
            }
        }
        /* Right Resize */
        MouseArea
        {
            id: resizeRight
            width: 5
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            anchors.rightMargin: 0
            anchors.bottomMargin: 10
            anchors.topMargin: 10

            visible: !maximizeBtn.isWindowMaximized

            cursorShape: Qt.SizeHorCursor
            DragHandler
            {
                onActiveChanged: if(active && !maximizeBtn.isWindowMaximized)
                                     mainWindow.startSystemResize(Qt.RightEdge)
            }
        }
        /* Top Resize */
        MouseArea
        {
            id: resizeTop
            height: 5
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.topMargin: 0

            visible: !maximizeBtn.isWindowMaximized

            cursorShape: Qt.SizeVerCursor
            DragHandler
            {
                onActiveChanged: if(active && !maximizeBtn.isWindowMaximized)
                                     mainWindow.startSystemResize(Qt.TopEdge)
            }
        }
        /* Bottom Resize */
        MouseArea
        {
            id: resizeBottom
            height: 5
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 0

            visible: !maximizeBtn.isWindowMaximized

            cursorShape: Qt.SizeVerCursor
            DragHandler
            {
                onActiveChanged: if(active && !maximizeBtn.isWindowMaximized)
                                     mainWindow.startSystemResize(Qt.BottomEdge)
            }
        }

        Connections
        {
            target: backend

            function onInternetConnected(connected)
            {
                internetConnected = connected
                if(!internetConnected)
                {
                    if(currectPage != "explore")
                    {
                        homeSearchSep.visible = false
                        searchExploreSep.visible = true
                        exploreAddSep.visible = true
                        addHelpSep.visible = true

                        homeBtn.btnDefaultColor = bgRec.color
                        searchInDBbtn.btnDefaultColor = topAreaRec.color
                        exploreBtn.btnDefaultColor = topAreaRec.color
                        addToDBbtn.btnDefaultColor = topAreaRec.color
                        helpBtn.btnDefaultColor = topAreaRec.color

                        if(currectPage != "home")
                        {
                            pagesStackView.push(Qt.resolvedUrl("pages/HomePage.qml"))
                            currectPage = "home"
                        }
                    }
                }
                else if(isFirstLoad)
                    isFirstLoad = false
            }

        }

}













