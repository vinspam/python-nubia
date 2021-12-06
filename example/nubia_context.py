#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#

from nubia import context, eventbus, exceptions


class NubiaExampleContext(context.Context):
    def on_connected(self, *args, **kwargs):
        pass

    async def on_cli(self, cmd, args):
        # dispatch the on connected message
        self.verbose = args.verbose
        await self.registry.dispatch_message(eventbus.Message.CONNECTED)

    async def on_interactive(self, args):
        self.verbose = args.verbose
        ret = await self._registry.find_command("connect").run_cli(args)
        if ret:
            raise exceptions.CommandError("Failed starting interactive mode")
        # dispatch the on connected message
        await self.registry.dispatch_message(eventbus.Message.CONNECTED)
