# slowstarter

[![Docker Repository on Quay](https://quay.io/repository/gnur/slowstarter/status "Docker Repository on Quay")](https://quay.io/repository/gnur/slowstarter)

This starts a webserver with a configurable "healthy" delay.

It exposes 3 endpoints:

- /
  - is healthy (status 200) right away
- /delayedHealthy
  - will become healthy *$DELAY_SECONDS* after starting
- /delayedUnhealthy
  - will become unhealthy (status 500) *$DELAY_SECONDS* after starting

If *$DELAY_SECONDS* is not set, it defaults to 10 seconds.
