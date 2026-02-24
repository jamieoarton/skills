# Get List Custom Fields

View the Custom Fields you have access to in a specific List.

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
    "/v2/list/{list_id}/field": {
      "get": {
        "summary": "Get List Custom Fields",
        "tags": [
          "Custom Fields"
        ],
        "description": "View the Custom Fields you have access to in a specific List.",
        "operationId": "GetAccessibleCustomFields",
        "parameters": [
          {
            "name": "list_id",
            "in": "path",
            "description": "",
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
            "name": "Content-Type",
            "in": "header",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "const": "application/json",
              "type": "string",
              "examples": [
                "application/json"
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
                  "title": "GetAccessibleCustomFieldsresponse",
                  "required": [
                    "fields"
                  ],
                  "type": "object",
                  "properties": {
                    "fields": {
                      "type": "array",
                      "items": {
                        "title": "Field",
                        "required": [
                          "id",
                          "name",
                          "type",
                          "type_config",
                          "date_created",
                          "hide_from_guests"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "type": {
                            "type": "string"
                          },
                          "type_config": {
                            "title": "TypeConfig",
                            "type": "object",
                            "properties": {
                              "options": {
                                "type": "array",
                                "items": {
                                  "title": "Option",
                                  "required": [
                                    "id",
                                    "color"
                                  ],
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "string"
                                    },
                                    "label": {
                                      "type": "string"
                                    },
                                    "color": {
                                      "type": [
                                        "string",
                                        "null"
                                      ]
                                    },
                                    "name": {
                                      "type": "string"
                                    },
                                    "value": {
                                      "type": "integer",
                                      "contentEncoding": "int32"
                                    },
                                    "type": {
                                      "type": "string"
                                    },
                                    "orderindex": {
                                      "type": "integer",
                                      "contentEncoding": "int32"
                                    }
                                  },
                                  "examples": [
                                    {
                                      "id": "fb332c98-d7bc-4ee8-a3bd-b5ffaff98c3c",
                                      "label": "one",
                                      "color": null
                                    }
                                  ]
                                },
                                "description": ""
                              },
                              "default": {
                                "oneOf": [
                                  {
                                    "type": [
                                      "string",
                                      "null"
                                    ]
                                  },
                                  {
                                    "type": "integer",
                                    "contentEncoding": "int32"
                                  },
                                  {}
                                ]
                              },
                              "precision": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "currency_type": {
                                "type": "string"
                              },
                              "placeholder": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "end": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "start": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "count": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "code_point": {
                                "type": "string"
                              },
                              "tracking": {
                                "title": "Tracking",
                                "required": [
                                  "subtasks",
                                  "checklists",
                                  "assigned_comments"
                                ],
                                "type": "object",
                                "properties": {
                                  "subtasks": {
                                    "type": "boolean"
                                  },
                                  "checklists": {
                                    "type": "boolean"
                                  },
                                  "assigned_comments": {
                                    "type": "boolean"
                                  }
                                },
                                "examples": [
                                  {
                                    "subtasks": true,
                                    "checklists": true,
                                    "assigned_comments": true
                                  }
                                ]
                              },
                              "complete_on": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              }
                            },
                            "examples": [
                              {}
                            ]
                          },
                          "date_created": {
                            "type": "string"
                          },
                          "hide_from_guests": {
                            "type": "boolean"
                          }
                        },
                        "examples": [
                          {
                            "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
                            "name": "Text Field",
                            "type": "text",
                            "type_config": {},
                            "date_created": "1566400407303",
                            "hide_from_guests": false
                          }
                        ]
                      },
                      "description": ""
                    }
                  }
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
      "name": "Custom Fields"
    }
  ]
}
```