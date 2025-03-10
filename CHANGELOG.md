# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Beta-1] - 01-23-2024

### Added
- Github action for building containers [#26](https://github.com/ncsa/standalone-smm-analytics/issues/26)
- Github action for manually building containers [#94](https://github.com/ncsa/standalone-smm-analytics/issues/94)
- Docker compose file for clowder connection [#88](https://github.com/ncsa/standalone-smm-analytics/issues/88)

### Changed
- Reorganized repository structure [#10](https://github.com/ncsa/standalone-smm-analytics/issues/10)

### Fixed
- Rabbitmq username and password [#61](https://github.com/ncsa/standalone-smm-analytics/issues/90)


## [Beta] - 10-26-2023

### Added
- Docker building script for whole components [#23](https://github.com/ncsa/standalone-smm-analytics/issues/23)
- Docker compose launch script [#45](https://github.com/ncsa/standalone-smm-analytics/issues/45)
- Docker compose file using traefik [#46](https://github.com/ncsa/standalone-smm-analytics/issues/46)
- Environment variables for turn on off twitter and reddit [#73](https://github.com/ncsa/standalone-smm-analytics/issues/73)
- Environment variable for Google Analytics 4 [#81](https://github.com/ncsa/standalone-smm-analytics/issues/81)

### Changed
- Hard coded rabbitmq url changed to env variable [#18](https://github.com/ncsa/standalone-smm-analytics/issues/18)
- Modified S3 url to env variable [#21](https://github.com/ncsa/standalone-smm-analytics/issues/21)
- Renamed Minio related environment variables [#31](https://github.com/ncsa/standalone-smm-analytics/issues/31)
- Rabbitmq handler's connection with dynamic credentials [#41](https://github.com/ncsa/standalone-smm-analytics/issues/41)
- Docker compose file to work with new settings [#42](https://github.com/ncsa/standalone-smm-analytics/issues/42)
- Updated README with docker compose information [#50](https://github.com/ncsa/standalone-smm-analytics/issues/50)
- Created base image for sentiment analysis with model [#55](https://github.com/ncsa/standalone-smm-analytics/issues/55)
- Created base image for name entity recognition with model [#56](https://github.com/ncsa/standalone-smm-analytics/issues/56)
- Docker compose file updated to fix minio default bucket making [#63](https://github.com/ncsa/standalone-smm-analytics/issues/63)
