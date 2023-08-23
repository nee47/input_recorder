import QtQuick 2.5
import QtQuick.Controls 2.5

Window {
    visible: true
    width: 400
    height: 300
    maximumHeight: 300
    maximumWidth: 400

    title: "Input Recorder by Joseph Vilca"

    Row {
        id: buttons
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: parent.top
        anchors.topMargin: 10
        anchors.leftMargin: 10
        spacing: 8

        Button {
            id: boton3
            text: qsTr("x")

            leftPadding: 30
            rightPadding: 30
            topPadding: 20
            bottomPadding: 20

        }

        Button {
            id: button4
            text: qsTr("y")

            leftPadding: 30
            rightPadding: 30
            topPadding: 20
            bottomPadding: 20
        }
    }


}
