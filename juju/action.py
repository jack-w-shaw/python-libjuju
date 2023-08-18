# Copyright 2023 Canonical Ltd.
# Licensed under the Apache V2, see LICENCE file for details.

from . import model


class Action(model.ModelEntity):
    @property
    def status(self):
        return self.data['status']

    async def wait(self):
        return await self.model.wait_for_action(self.id)
