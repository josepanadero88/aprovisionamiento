pipeline {
    agent any

    environment {
        // ID de la BUILD
        BUILD_ID = "${env.BUILD_NUMBER}"
        WEB_REPO_URL = "git@git.virt.cga:japanadero/aprovisionamiento.git"
    }

    stages {
        stage("Preparando entorno (build)") {
            steps {
                deleteDir()
                dir('web-repo') {
                  git branch: 'testing',
                  url: "${env.WEB_REPO_URL}",
                  credentialsId: 'usuario'
                }

                sh 'cd docker && docker-compose up -d --build'
            }
        }

        stage("Desplegando configuración (deploy)") {
            steps {
                // Pasamos el build_id a Ansible para que lo inyecte en el HTML
                sh "docker exec web-preproduccion ansible-playbook /ansible/playbook.yml -e 'build_id=${BUILD_ID}'"
            }
        }
        stage("Realizando pruebas (testing)") {
            steps {
                // 1. Ejecutamos el test desde el contenedor cliente
                // 2. Usamos pytest para generar el reporte XML JUnit
                sh 'docker exec cliente pytest /ansible/test_web.py --junitxml=/ansible/results.xml'
            }
        }
    }

    post {
        always {
            // Jenkins publica el resultado JUnit
            // Copiamos el XML del contenedor a la VM para que Jenkins lo vea
            // opcion true, test falla = docker cp da error, true omite error y continua pipeline
            sh 'docker cp cliente:/ansible/results.xml || true '
            junit 'results.xml'
        }

        success {
            // CUMPLIMOS: "El merge a master solo puede hacerlo Jenkins de manera automática"
            // git checkout master || git checkout -b master, si no puede cambiar de rama, la crea, suele fallar la 1 vez
            echo "Pruebas exitosas. Realizando promoción a master..."
                dir('web-repo') {
                  sshagent(['usuario']) { // sshagent nos permite usar llave SSH para push
                      usuario@ubuntu:~/proyecto-despliegues/aprovisionamiento$ cat Jenkinsfile 
pipeline {
    agent any

    environment {
        // ID de la BUILD
        BUILD_ID = "${env.BUILD_NUMBER}"
        WEB_REPO_URL = "git@git.virt.cga:japanadero/aprovisionamiento.git"
    }

    stages {
        stage("Preparando entorno (build)") {
            steps {
                deleteDir()
                dir('web-repo') {
                  git branch: 'testing',
                  url: "${WEB_REPO_URL},
                  credentialsId: 'usuario'
                }

                sh 'cd docker && docker-compose up -d --build'
            }
        }

        stage("Desplegando configuración (deploy)") {
            steps {
                // Pasamos el build_id a Ansible para que lo inyecte en el HTML
                sh "docker exec web-preproduccion ansible-playbook /ansible/playbook.yml -e 'build_id=${BUILD_ID}'"
            }
        }
        stage("Realizando pruebas (testing)") {
            steps {
                // 1. Ejecutamos el test desde el contenedor cliente
                // 2. Usamos pytest para generar el reporte XML JUnit
                sh 'docker exec cliente pytest /ansible/test_web.py --junitxml=/ansible/results.xml'
            }
        }
    }

    post {
        always {
            // Jenkins publica el resultado JUnit
            // Copiamos el XML del contenedor a la VM para que Jenkins lo vea
            // opcion true, test falla = docker cp da error, true omite error y continua pipeline
            sh 'docker cp cliente:/ansible/results.xml || true '
            junit 'results.xml'
        }

        success {
            // CUMPLIMOS: "El merge a master solo puede hacerlo Jenkins de manera automática"
            // git checkout master || git checkout -b master, si no puede cambiar de rama, la crea, suele fallar la 1 vez
            echo "Pruebas exitosas. Realizando promoción a master..."
                dir('web-repo') {
                  sshagent(['usuario']) { // sshagent nos permite usar llave SSH para push
                      sh '''
                          git config user.email "jenkins@despliegue.es"
                          git config user.name "jenkins panadero"
                          git checkout master || git checkout -b master
                          git merge origin/testing
                          git push origin master
                      '''
                }
            }
        }
    }
}

                git config user.email "jenkins@despliegue.es"
                git config user.name "jenkins panadero"
                git checkout master || git checkout -b master
                git merge origin/testing
                git push origin master
            '''
                }
            }
        }
    }
}
