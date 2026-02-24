# Get Custom Roles

View the Custom Roles available in a Workspace.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_id}/customroles": {
      "get": {
        "summary": "Get Custom Roles",
        "tags": [
          "Roles"
        ],
        "description": "View the Custom Roles available in a Workspace.",
        "operationId": "GetCustomRoles",
        "parameters": [
          {
            "name": "team_id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "include_members",
            "in": "query",
            "description": "",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "GetCustomRolesresponse",
                  "required": [
                    "custom_roles"
                  ],
                  "type": "object",
                  "properties": {
                    "custom_roles": {
                      "type": "array",
                      "items": {
                        "title": "CustomRole2",
                        "required": [
                          "id",
                          "team_id",
                          "name",
                          "inherited_role",
                          "date_created",
                          "members"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "team_id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "inherited_role": {
                            "type": "integer",
                            "contentEncoding": "int32"
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "members": {
                            "type": "array",
                            "items": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "description": ""
                          }
                        },
                        "examples": [
                          {
                            "id": 4547089,
                            "team_id": "301539",
                            "name": "guest custom",
                            "inherited_role": 4,
                            "date_created": "1651189835671",
                            "members": [
                              12345,
                              67899
                            ]
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "custom_roles": [
                        {
                          "id": 4547089,
                          "team_id": "301539",
                          "name": "guest custom",
                          "inherited_role": 4,
                          "date_created": "1651189835671",
                          "members": [
                            12345,
                            67899
                          ]
                        },
                        {
                          "id": 6715664,
                          "team_id": "301539",
                          "name": "member custom",
                          "inherited_role": 3,
                          "date_created": "1651189901020",
                          "members": [
                            5553,
                            98989
                          ]
                        },
                        {
                          "id": 2957195,
                          "team_id": "301539",
                          "name": "admin custom",
                          "inherited_role": 2,
                          "date_created": "1651189904868",
                          "members": [
                            47474,
                            818181
                          ]
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "custom_roles": [
                    {
                      "id": 4547089,
                      "team_id": "301539",
                      "name": "guest custom",
                      "inherited_role": 4,
                      "date_created": "1651189835671",
                      "members": [
                        12345,
                        67899
                      ]
                    },
                    {
                      "id": 6715664,
                      "team_id": "301539",
                      "name": "member custom",
                      "inherited_role": 3,
                      "date_created": "1651189901020",
                      "members": [
                        5553,
                        98989
                      ]
                    },
                    {
                      "id": 2957195,
                      "team_id": "301539",
                      "name": "admin custom",
                      "inherited_role": 2,
                      "date_created": "1651189904868",
                      "members": [
                        47474,
                        818181
                      ]
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Roles"
    }
  ]
}
```