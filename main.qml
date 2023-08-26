import QtQuick 2.5
import QtQuick.Controls 2.5

Window {
    id: mainWindow
    visible: true
    width: 400
    height: 150
    maximumHeight: 150
    maximumWidth: 400

    title: "Input Recorder by Joseph Vilca"


    Row {
        id: buttons
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 10
        anchors.leftMargin: 10
        spacing: 12

        property int buttonWidth: 100

        Button {
            id: boton1
            text: qsTr("PLAY")
            width: parent.buttonWidth
            height: 80
        }

        Button {
            id: button2
            text: qsTr("RECORD")

            width: parent.buttonWidth
            height: 80
        }
    }

    Row{
        id: labels
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: buttons.bottom
        anchors.topMargin: 10
        spacing: 20
        Label{
            text: qsTr("PLAY = ATAJO")
        }

        Label{
            text: qsTr("RECORD = ATAJO")
        }
    }
}
