<template>
    <tr>
        <th>
            <router-link
                :to="{name: 'protocol', params: {protocol: protocol.name}}"
            >
                {{ protocol.name }}
            </router-link>
        </th>
        <td>
            {{ protocol.nodes.length }}
        </td>
        <td>
            <div v-if="statsProtocolToday">
                {{ statsProtocolToday.usersTotal }}
            </div>
        </td>
    </tr>
</template>

<script>
import gql from 'graphql-tag'


const statsQuery = gql`
    query ProtocolStats($name: String!) {
        statsProtocolToday(name: $name) {
            usersTotal
        }
    }
`

export default {
    apollo: {
        statsProtocolToday: {
            query: statsQuery,
            variables() {
                return {
                    name: this.protocol.name,
                }
            },
        },
    },
    name: "ProtocolTableRow",
    props: {
        protocol: {
            type: Object,
            default: null,
        },
    },
    data() {
        return {
            statsProtocolToday: {},
        }
    },
}
</script>
