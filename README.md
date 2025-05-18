# YADRO-Impulse-2025-Telecom-DevOps

---

# Установка зависимостей и запуск

`sudo apt update`

`sudo apt install -y software-properties-common git`

`sudo add-apt-repository --yes --update ppa:ansible/ansible`

`sudo apt install -y ansible `

`git clone https://github.com/sem36/YADRO-Impulse-2025-Telecom-DevOps.git`

`cd YADRO-Impulse-2025-Telecom-DevOps`

`ansible-playbook -i inventory playbook.yml`

---
# Результат

в ходе выполнения столкунлся с проблемой того что команда docker logs выводит данные на stderr, когда внутри контейнера используется logging с выводом в stderr. А Ansible по умолчанию сохраняет только stdout, решил данную проблему путём обединения
