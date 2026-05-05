pipeline {
    agent any
    stages {
        stage("Preparando entorno (build)") {
            steps {
                // Levanta los contenedores
                sh 'cd docker && docker-compose up -d --build'
            }
        }
        stage("Desplegando configuración (deploy)") {
            steps {
                // Ejecuta Ansible DENTRO del contenedor web
                sh 'docker exec web-preproduccion ansible-playbook /ansible/playbook.yml'
            }
        }
        stage("Realizando pruebas (testing)") {
            steps {
                // El cliente hace la petición al servidor
                sh "docker exec cliente curl -s http://web-preproduccion:8083 | grep "[japanadero]""
                // Aquí se generaría el reporte JUnit XML
            }
        }
    }
    post {
        success {
            // Solo si todo es verde, se hace el merge a master
            echo "Pruebas exitosas. Realizando promoción a master..."
            // (Comandos de git para merge automático)
        }
    }
}