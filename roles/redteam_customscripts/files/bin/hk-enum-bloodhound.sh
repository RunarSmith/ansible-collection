#!/bin/bash

echo "before the first connexion, open a web browser and go to : http://localhost:7474"
echo "and initilise password"
echo "initial credential: neo4j / neo4j"
echo ""
echo "actual credentials: neo4j / parrot"

sudo neo4j start

# give it 5 seconds to start
sleep 5

bloodhound
